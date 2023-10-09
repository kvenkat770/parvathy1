from enum import Enum

class QueryLists:
    BLACKLIST = ['victim_ip_lower', 'victim_ip_upper']


class Audit:
    VALID_PAGE_NAMES = ('dashboard', 'attack_details', 'reports', 'ip_block_list')


class HeaderConstants:
    TENANT_ID = "x-tenant-id"
    USER_ID = "x-user-id"
    AUTHORIZATION = "authorization"


class HttpStatusCodes:
    FORBIDDEN = 403
    NOT_FOUND = 404
    UNAUTHORIZED = 401
    BAD_REQUEST = 400
    OK = 200
    PERMANENT_REDIRECT = 308


class HttpMimeTypes:
    JSON = "application/json"
    PLAINTEXT = "text/plain"


class QueryStringOperators:
    GREATER = "gt"
    LESSER = "lt"
    GREATER_EQUALS = "gte"
    LESSER_EQUALS = "lte"
    EQUALS = "eq"
    NOT_EQUALS = "neq"
    CONTAINS = "contains"
    IN = "in"

class PaginationSortField:
    fields = {'Default': 'id', 'WeaponizedIP': 'timestamp', 'AttackSummary': 'id'}


class OrderBy(Enum):
    desc = "True"


class YieldPer(Enum):
    batch_size_10000 = 10000
    batch_size_50000 = 50000


class Pagination(Enum):
    page_num = "1"
    page_size = "25"


class DatabaseConstants(Enum):
    ID = "id"
    VICTIM_ORG = "victim_org"
    VICTIM_PORTS = "victim_ports"
    VICTIM_LONGITUDE = "victim_longitude"
    ATTACK_SIZE_BANDWIDTH = "attack_size_bandwidth"
    VICTIM_LATITUDE = "victim_latitude"
    START_TIME = "start_time"
    LAST_UPDATE_TIME = "last_update_time"
    ATTACK_TYPE = "attack_type"
    VICTIM_ASN = "victim_asn"
    ONGOING = "ongoing"
    VICTIM_CITY = "victim_city"
    DURATION = "duration"
    HOSTNAMES = "hostnames"
    VICTIM_IP_RANGE = "victim_ip_range"
    VICTIM_COUNTRY = "victim_country"
    ATTACK_SIZE_PPS = "attack_size_pps"
    VICTIM_BUSINESS_VERTICAL = "victim_business_vertical"


class WeaponizedIPDBConstants(Enum):
    ID = "_id"
    RECORD_DATE = "record_date"
    TIMESTAMP = "timestamp"


class Trends:
    COUNTRY = "country"
    VICTIM_IP_RANGE = "victim_ip_range"
    ATTACK_TYPE = "attack_type"
    WEAPON_TYPE = "weapon_type"
    ASN = "asn"
    ORG = "org"
    PORT = "port"
    URI = "uri"
    COMMAND = "command"
    ORG_TYPE = "org-type"
    MALWARE_HASH = "malware-hash"
    MALWARE_IP_ADDRESS = "malware-ip-address"


class AmplificationStatsFiles:
    TOP_20_COUNTRIES = "data/amplification_weapons_top_20_countries.json"
    TOP_20_ORGS = "data/amplification_weapons_top_20_orgs.json"
    TOP_20_WEAPON_TYPE = "data/amplification_weapons_top_20_weapon_type.json"


class DronesStatsFiles:
    TOP_20_COUNTRIES = "data/drones_top_20_countries.json"
    TOP_20_ORGS = "data/drones_top_20_orgs.json"
    TOP_20_URI = "data/drones_top_20_uri.json"
    TOP_20_MIRAI = "data/drones_top_20_mirai_port.json"


class VulnExploitStatsFiles:
    TOP_VULN_EXPLOIT_ATTEMPTS = "data/top_vuln_exploit_attempts.json"


class MalwareStatsFiles:
    IP_ADDRESS_BY_COUNTRIES = "data/malware_ips_by_countries.json"
    IP_ADDRESS_BY_ORGANIZATION = "data/malware_ips_by_organization.json"
    IP_ADDRESS_BY_ORGANIZATION_TYPE = "data/malware_ips_by_organization_type.json"
    TOP_MALWARE_HASH = "data/top_malware_hashes.json"
    TOP_MALWARE_IP_ADDRESS = "data/top_malware_ips.json"

class AmplifierPortTypes:
    KNOWN_LOW_PORT = 1
    KNOWN_HIGH_PORT = 2
    RANDOM_HIGH_PORT = 3


class ThreatListsSubstrings(Enum):
    FORMAT_SUBSTRING = "_format-"
    COUNTRY_SUBSTRING = "_country-"


class ThreatListsFormats(Enum):
    FORMAT_IPV4_HOST = "ipv4host"
    FORMAT_IPV6_HOST = "ipv6host"
    FORMAT_IPV4_NETWORK = "ipv4network"


class ThreatListsCountries(Enum):
    COUNTRY_ALL = "all"


PortTypeToAmplifierMap = {
    "opendns": 1,
    "mikrotik": 2,
    "ssdp": 3,
    "opensnmp": 1,
    "portmap": 1,
    "snmp": 1,
    "tftp": 1,
    "dns": 1,
    "openvpn": 2,
    "netbios": 1,
    "wsdiscovery": 3,
    "coap": 3,
    "rip": 1,
    "mdns": 3,
    "natpmp": 2,
    "ntp": 1,
    "mssql": 2,
    "dahua-udp": 2,
    "ubiquiti": 2
}

COUNTRIES = [
'Afghanistan',
'Albania',
'Algeria',
'American Samoa',
'Andorra',
'Angola',
'Anguilla',
'Antarctica',
'Antigua and Barbuda',
'Argentina',
'Armenia',
'Aruba',
'Australia',
'Austria',
'Azerbaijan',
'Bahamas',
'Bahrain',
'Bangladesh',
'Barbados',
'Belarus',
'Belgium',
'Belize',
'Benin',
'Bermuda',
'Bhutan',
'Bolivia',
'Bonaire, Sint Eustatius, and S',
'Bosnia and Herzegovina',
'Botswana',
'Bouvet Island',
'Brazil',
'British Indian Ocean Territory',
'British Virgin Islands',
'Brunei',
'Bulgaria',
'Burkina Faso',
'Burundi',
'Cabo Verde',
'Cambodia',
'Cameroon',
'Canada',
'Cayman Islands',
'Central African Republic',
'Chad',
'Chile',
'China',
'Christmas Island',
'Cocos (Keeling) Islands',
'Colombia',
'Comoros',
'Congo Republic',
'Cook Islands',
'Costa Rica',
'Croatia',
'Cuba',
'Curaçao',
'Cyprus',
'Czechia',
'DR Congo',
'Denmark',
'Djibouti',
'Dominica',
'Dominican Republic',
'Ecuador',
'Egypt',
'El Salvador',
'Equatorial Guinea',
'Eritrea',
'Estonia',
'Eswatini',
'Ethiopia',
'Falkland Islands',
'Faroe Islands',
'Fiji',
'Finland',
'France',
'French Guiana',
'French Polynesia',
'French Southern Territories',
'Gabon',
'Georgia',
'Germany',
'Ghana',
'Gibraltar',
'Greece',
'Greenland',
'Grenada',
'Guadeloupe',
'Guam',
'Guatemala',
'Guernsey',
'Guinea',
'Guinea-Bissau',
'Guyana',
'Haiti',
'Heard and McDonald Islands',
'Honduras',
'Hong Kong',
'Hungary',
'Iceland',
'India',
'Indonesia',
'Iran',
'Iraq',
'Ireland',
'Isle of Man',
'Israel',
'Italy',
'Ivory Coast',
'Jamaica',
'Japan',
'Jersey',
'Jordan',
'Kazakhstan',
'Kenya',
'Kiribati',
'Kosovo',
'Kuwait',
'Kyrgyzstan',
'Laos',
'Latvia',
'Lebanon',
'Lesotho',
'Liberia',
'Libya',
'Liechtenstein',
'Lithuania',
'Luxembourg',
'Macao',
'Madagascar',
'Malawi',
'Malaysia',
'Maldives',
'Mali',
'Malta',
'Marshall Islands',
'Martinique',
'Mauritania',
'Mauritius',
'Mayotte',
'Mexico',
'Micronesia',
'Moldova',
'Monaco',
'Mongolia',
'Montenegro',
'Montserrat',
'Morocco',
'Mozambique',
'Myanmar',
'Namibia',
'Nauru',
'Nepal',
'Netherlands',
'New Caledonia',
'New Zealand',
'Nicaragua',
'Niger',
'Nigeria',
'Niue',
'Norfolk Island',
'North Korea',
'North Macedonia',
'Northern Mariana Islands',
'Norway',
'Oman',
'Pakistan',
'Palau',
'Palestine',
'Panama',
'Papua New Guinea',
'Paraguay',
'Peru',
'Philippines',
'Pitcairn Islands',
'Poland',
'Portugal',
'Puerto Rico',
'Qatar',
'Romania',
'Russia',
'Rwanda',
'Réunion',
'Saint Barthélemy',
'Saint Helena',
'Saint Lucia',
'Saint Martin',
'Saint Pierre and Miquelon',
'Samoa',
'San Marino',
'Saudi Arabia',
'Senegal',
'Serbia',
'Seychelles',
'Sierra Leone',
'Singapore',
'Sint Maarten',
'Slovakia',
'Slovenia',
'Solomon Islands',
'Somalia',
'South Africa',
'South Georgia and South Sandwi',
'South Korea',
'South Sudan',
'Spain',
'Sri Lanka',
'St Kitts and Nevis',
'St Vincent and Grenadines',
'Sudan',
'Suriname',
'Svalbard and Jan Mayen',
'Sweden',
'Switzerland',
'Syria',
'São Tomé and Príncipe',
'Taiwan',
'Tajikistan',
'Tanzania',
'Thailand',
'The Gambia',
'Timor-Leste',
'Togo',
'Tokelau',
'Tonga',
'Trinidad and Tobago',
'Tunisia',
'Turkey',
'Turkmenistan',
'Turks and Caicos Islands',
'Tuvalu',
'U.S. Outlying Islands',
'U.S. Virgin Islands',
'Uganda',
'Ukraine',
'United Arab Emirates',
'United Kingdom',
'United States',
'Uruguay',
'Uzbekistan',
'Vanuatu',
'Vatican City',
'Venezuela',
'Vietnam',
'Wallis and Futuna',
'Western Sahara',
'Yemen',
'Zambia',
'Zimbabwe',
'Åland'
]

VICTIM_TAGS = ["database", "cryptocurrency", "videogame", "cloud", "vpn", "cdn"]

ATTACK_TYPES = ["ARM", "CHARGEN", "CLDAP", "CoAP", "DB2", "DNS", "DTLS", "Dahua-37810",
                "Jenkins", "KNX", "LDAP", "MSSQL", "Memcache", "Mikrotik-2000", "Mumble", "NATPMP", "NTP",
                "NetBIOS", "Netis", "OpenVPN", "Plexmedia-32414", "Portmap", "QOTD", "Quake3", "RDP", "Rockwell",
                "SLP", "SNMP", "SNMPv2", "SSDP", "TFTP", "TP240DVR", "Ubiquiti", "VSE-21025", "VSE-2303",
                "VSE-27015", "VSE-27016", "VSE-27019", "VSE-28015", "WDBRPC", "WSDiscovery", "mDNS"]
