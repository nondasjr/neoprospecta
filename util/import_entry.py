import urllib.request
import gzip


from neoprospecta.biology.models import Entry, Specie, Kingdom
from neoprospecta.parameter.models import EntryParameter
from django_rq import job

class Process():
    content = None
    entries = []
    url = 'https://www.arb-silva.de/fileadmin/silva_databases/release_128/Exports/SILVA_128_LSURef_tax_silva.fasta.gz'
    row_start = 0
    row_end = 5000


    def run(self):
        self.set_parameter()
        self.get_release()
        self.get_entries()

    def  set_parameter(self):
        """Considera sempre o ultimo parametro registrado"""
        param = EntryParameter.objects.last()
        if param:
            self.url = param.url
            self.row_start = param.row_start
            self.row_end = param.row_end

    def get_release(self):
        """busca as entry de acordo com o parametro"""
        with urllib.request.urlopen(self.url) as response:
            with gzip.GzipFile(fileobj=response) as uncompressed:
                self.content = uncompressed.read()


    def get_entries(self):
        """Processa as entry e salva no banco de dados
           Considera a primeira linha como informação da entry
           e da segunda linha em diante como sequencia RNA/DNA
           O parametro de quantidade deve ser definido em Parameter Entry
        """
        self.entries = self.content.decode("utf-8").split('>')[self.row_start+1:self.row_end+1]
        for entry in self.entries:
            entry = entry.split('\n')
            if entry:
                access_id = self.get_access_id(entry)
                if self.is_valide_access_id(access_id):
                    kingdom = self.get_kingdom(entry)
                    sequence = self.get_sequence(entry)
                    species = self.get_especies(entry)
                    tmp_entry, created = Entry.objects.get_or_create(
                        access_id = access_id,
                        kingdom = kingdom,
                        sequence = sequence
                    )
                    tmp_entry.specie.add(*species)
                    tmp_entry.save()

    def is_valide_access_id(self, access_id):
        """Valida se a access_id é unica, deve-se desconsiderar a entry que já existe"""
        return not Entry.objects.filter(access_id=access_id).exists()

    def get_sequence(self, entry):
        """Sempre peg a primeira sequencia que vem na segunda posição do array
           Returns:
               'UAUUUUUUUAAAGGGCGUUAUAGGGCUGCCUAGGUAUUAAAAAAAAGAGUUGUGUAUUGCAAUAAGUAGAUUUGAAGAUA'
        """
        return entry[1]

    def get_access_id(self, entry):
        """Retorna o access_id considerando ser o primeiro item quando quebrado por espaço
           Returns:
               'GAXI01000525.2981.5481'
        """
        return entry[0].split(' ')[0]

    def get_kingdom(self, entry):
        """Busca o label do kingdom e valida se ele já existe, se não cria um com o novo label
           Returns:
               Kingdom Object
               example:
               {
                'id': 1,
                'label': 'Bacteria'
               }
        """
        label = entry[0].split(' ')[1].split(';')[0]
        kingdom, created = Kingdom.objects.get_or_create(label=label)
        return kingdom

    def get_especies(self, entry):
        """Busca o label do kingdom e valida se ele já existe, se não cria um com o novo label
           Returns:
               Array de Specie Object
               example:
               [{
                'id': 1,
                'label': 'Rickettsiales'
               }]
        """
        especies_label = entry[0].split(' ')[1].split(';')[1:]
        species = []

        for label in especies_label:
            especie, created = Specie.objects.get_or_create(label=label)
            species.append(especie)

        return species


@job
def process_entry():
    process = Process()
    process.run()