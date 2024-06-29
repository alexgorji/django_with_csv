from pathlib import Path
from unittest import TestCase
import pandas
from pandas import DataFrame
import json

csv_path = Path(__file__).parent.parent / 'csv'


class TestCSVImport(TestCase):
    def setUp(self):
        self.csv = pandas.read_csv(csv_path / '2024_1_GLS.csv', sep=';')

    def test_type(self):
        assert isinstance(self.csv, DataFrame)

    def test_headers(self):
        assert self.csv.columns.tolist() == ['Buchungstag', 'Name Zahlungsbeteiligter', 'Buchungstext',
                                             'Verwendungszweck', 'Betrag', 'Waehrung']

    def test_json(self):
        data = json.loads(self.csv.to_json())
        assert data == {'Buchungstag': {'0': '31.01.2024', '1': '30.01.2024', '2': '25.01.2024', '3': '23.01.2024',
                                        '4': '23.01.2024', '5': '17.01.2024', '6': '12.01.2024', '7': '03.01.2024'},
                        'Name Zahlungsbeteiligter': {'0': None, '1': 'PayPal Europe S.a.r.l. et Cie S.C.A',
                                                     '2': 'PayPal Europe S.a.r.l. et Cie S.C.A',
                                                     '3': 'Bundeskasse - Dienstort Weiden -',
                                                     '4': 'Bundeskasse - Dienstort Weiden -',
                                                     '5': 'Bundeskasse - Dienstort Weiden -',
                                                     '6': 'Bundeskasse - Dienstort Weiden -',
                                                     '7': 'PayPal Europe S.a.r.l. et Cie S.C.A'},
                        'Buchungstext': {'0': 'Abschluss', '1': 'Basislastschrift', '2': 'Basislastschrift',
                                         '3': 'Überweisungsgutschr.', '4': 'Überweisungsgutschr.',
                                         '5': 'Überweisungsgutschr.',
                                         '6': 'Überweisungsgutschr.', '7': 'Basislastschrift'},
                        'Verwendungszweck': {'0': 'Abschluss per 31.01.2024',
                                             '1': '1032146679097/PP.5849.PP/. , Ihr Einkauf bei EREF: 1032146679097 MREF: 5JEJ2257BAP2L CRED: LU96ZZZ0000000000000000058 IBAN: LU89751000135104200E BIC: PPLXLUL2',
                                             '2': '1032091768597/PP.5849.PP/. Apple Services, Ihr Einkauf bei Apple Services EREF: 1032091768597 MREF: 5JEJ2257BAP2L CRED: LU96ZZZ0000000000000000058 IBAN: LU89751000135104200E BIC: PPLXLUL2',
                                             '3': 'RNR. 000166413 EREF: 06-03106397-0003726830-24037-004129',
                                             '4': 'RNR. 000165930 EREF: 06-03106397-0003726830-24037-003647',
                                             '5': 'RNR. 000165798 EREF: 06-03106397-0003726830-24033-004121',
                                             '6': 'RNR. 000164444 EREF: 06-03106397-0003726830-24028-002058',
                                             '7': '1031585262471/PP.5849.PP/. , Ihr Einkauf bei EREF: 1031585262471 MREF: 5JEJ2257BAP2L CRED: LU96ZZZ0000000000000000058 IBAN: LU89751000135104200E BIC: PPLXLUL2'},
                        'Betrag': {'0': '-3,80', '1': '-40,00', '2': '-0,99', '3': '201,87', '4': '394,92',
                                   '5': '109,80',
                                   '6': '182,97', '7': '-913,98'},
                        'Waehrung': {'0': 'EUR', '1': 'EUR', '2': 'EUR', '3': 'EUR', '4': 'EUR', '5': 'EUR', '6': 'EUR',
                                     '7': 'EUR'}}
