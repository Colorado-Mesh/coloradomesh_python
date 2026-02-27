from typing import Any

from denvermesh.colorado._base import _Place, _PlaceEnum, PlaceAbbreviations


class Municipality(_Place):
    def __init__(self, /, **data: Any):
        super().__init__(**data)


class Municipalities(_PlaceEnum):
    AGUILAR = Municipality(
        name="Aguilar",
        abbreviations=PlaceAbbreviations(
            three_letter="AGU",
            five_letter="AGULR",
            seven_letter="AGUILAR",
            fourteen_letter="AGUILAR"
        )
    )
    AKRON = Municipality(
        name="Akron",
        abbreviations=PlaceAbbreviations(
            three_letter="AKR",
            five_letter="AKRON",
            seven_letter="AKRON",
            fourteen_letter="AKRON"
        )
    )
    ALAMOSA = Municipality(
        name="Alamosa",
        abbreviations=PlaceAbbreviations(
            three_letter="AMS",
            five_letter="ALMSA",
            seven_letter="ALAMOSA",
            fourteen_letter="ALAMOSA"
        )
    )
    ALMA = Municipality(
        name="Alma",
        abbreviations=PlaceAbbreviations(
            three_letter="ALM",
            five_letter="ALMA",
            seven_letter="ALMA",
            fourteen_letter="ALMA"
        )
    )
    ANTONITO = Municipality(
        name="Antonio",
        abbreviations=PlaceAbbreviations(
            three_letter="ANT",
            five_letter="ANTNO",
            seven_letter="ANTNTO",
            fourteen_letter="ANTONITO"
        )
    )
    ARRIBA = Municipality(
        name="Arriba",
        abbreviations=PlaceAbbreviations(
            three_letter="ARB",
            five_letter="ARRBA",
            seven_letter="ARRIBA",
            fourteen_letter="ARRIBA"
        )
    )
    ARVADA = Municipality(
        name="Arvada",
        abbreviations=PlaceAbbreviations(
            three_letter="ARV",
            five_letter="ARVDA",
            seven_letter="ARVADA",
            fourteen_letter="ARVADA"
        )
    )
    ASPEN = Municipality(
        name="Aspen",
        abbreviations=PlaceAbbreviations(
            three_letter="ASP",
            five_letter="ASPEN",
            seven_letter="ASPEN",
            fourteen_letter="ASPEN"
        )
    )
    AULT = Municipality(
        name="Ault",
        abbreviations=PlaceAbbreviations(
            three_letter="ALT",
            five_letter="AULT",
            seven_letter="AULT",
            fourteen_letter="AULT"
        )
    )
    AURORA = Municipality(
        name="Aurora",
        abbreviations=PlaceAbbreviations(
            three_letter="AUR",
            five_letter="AURRA",
            seven_letter="AURORA",
            fourteen_letter="AURORA"
        )
    )
    AVON = Municipality(
        name="Avon",
        abbreviations=PlaceAbbreviations(
            three_letter="AVN",
            five_letter="AVON",
            seven_letter="AVON",
            fourteen_letter="AVON"
        )
    )
    BASALT = Municipality(
        name="Basalt",
        abbreviations=PlaceAbbreviations(
            three_letter="BST",
            five_letter="BSALT",
            seven_letter="BASALT",
            fourteen_letter="BASALT"
        )
    )
    BAYFIELD = Municipality(
        name="Bayfield",
        abbreviations=PlaceAbbreviations(
            three_letter="BYF",
            five_letter="BYFLD",
            seven_letter="BAYFLD",
            fourteen_letter="BAYFIELD"
        )
    )
    BENNETT = Municipality(
        name="Bennett",
        abbreviations=PlaceAbbreviations(
            three_letter="BNT",
            five_letter="BENNT",
            seven_letter="BENNETT",
            fourteen_letter="BENNETT"
        )
    )
    BERTHOUD = Municipality(
        name="Berthoud",
        abbreviations=PlaceAbbreviations(
            three_letter="BRT",
            five_letter="BRTHD",
            seven_letter="BERTHD",
            fourteen_letter="BERTHOUD"
        )
    )
    BETHUNE = Municipality(
        name="Bethune",
        abbreviations=PlaceAbbreviations(
            three_letter="BTH",
            five_letter="BTHNE",
            seven_letter="BETHUNE",
            fourteen_letter="BETHUNE"
        )
    )
    BLACK_HAWK = Municipality(
        name="Black Hawk",
        abbreviations=PlaceAbbreviations(
            three_letter="BLH",
            five_letter="BLKHK",
            seven_letter="BLKHAWK",
            fourteen_letter="BLACKHAWK"
        )
    )
    BLANCA = Municipality(
        name="Blanca",
        abbreviations=PlaceAbbreviations(
            three_letter="BLA",
            five_letter="BLNCA",
            seven_letter="BLANCA",
            fourteen_letter="BLANCA"
        )
    )
    BLUE_RIVER = Municipality(
        name="Blue River",
        abbreviations=PlaceAbbreviations(
            three_letter="BLR",
            five_letter="BLRVR",
            seven_letter="BLRIVER",
            fourteen_letter="BLUERIVER"
        )
    )
    BONANZA = Municipality(
        name="Bonanza",
        abbreviations=PlaceAbbreviations(
            three_letter="BNZ",
            five_letter="BNANZ",
            seven_letter="BONANZA",
            fourteen_letter="BONANZA"
        )
    )
    BOONE = Municipality(
        name="Boone",
        abbreviations=PlaceAbbreviations(
            three_letter="BNE",
            five_letter="BOONE",
            seven_letter="BOONE",
            fourteen_letter="BOONE"
        )
    )
    BOULDER = Municipality(
        name="Boulder",
        abbreviations=PlaceAbbreviations(
            three_letter="BDL",
            five_letter="BOULR",
            seven_letter="BOULDER",
            fourteen_letter="BOULDER"
        )
    )
    BOW_MAR = Municipality(
        name="Bow Mar",
        abbreviations=PlaceAbbreviations(
            three_letter="BWM",
            five_letter="BOWMR",
            seven_letter="BOWMAR",
            fourteen_letter="BOWMAR"
        )
    )
    BRANSON = Municipality(
        name="Branson",
        abbreviations=PlaceAbbreviations(
            three_letter="BRS",
            five_letter="BRNSN",
            seven_letter="BRANSON",
            fourteen_letter="BRANSON"
        )
    )
    BRECKENRIDGE = Municipality(
        name="Breckenridge",
        abbreviations=PlaceAbbreviations(
            three_letter="BCK",
            five_letter="BRECK",
            seven_letter="BRKNRDG",
            fourteen_letter="BRECKENRIDGE"
        )
    )
    BRIGHTON = Municipality(
        name="Brighton",
        abbreviations=PlaceAbbreviations(
            three_letter="BRT",
            five_letter="BRGHT",
            seven_letter="BRIGHTN",
            fourteen_letter="BRIGHTON"
        )
    )
    BROOKSIDE = Municipality(
        name="Brookside",
        abbreviations=PlaceAbbreviations(
            three_letter="BKS",
            five_letter="BRKSD",
            seven_letter="BROOKSD",
            fourteen_letter="BROOKSIDE"
        )
    )
    BROOMFIELD = Municipality(
        name="Broomfield",
        abbreviations=PlaceAbbreviations(
            three_letter="BRM",
            five_letter="BROOM",
            seven_letter="BROOMFD",
            fourteen_letter="BROOMFIELD"
        )
    )
    BRUSH = Municipality(
        name="Brush",
        abbreviations=PlaceAbbreviations(
            three_letter="BSH",
            five_letter="BRUSH",
            seven_letter="BRUSH",
            fourteen_letter="BRUSH"
        )
    )
    BUENA_VISTA = Municipality(
        name="Buena Vista",
        abbreviations=PlaceAbbreviations(
            three_letter="BVT",
            five_letter="BNVST",
            seven_letter="BNVISTA",
            fourteen_letter="BUENAVISTA"
        )
    )
    BURLINGTON = Municipality(
        name="Burlington",
        abbreviations=PlaceAbbreviations(
            three_letter="BRL",
            five_letter="BRLNG",
            seven_letter="BURLNGT",
            fourteen_letter="BURLINGTON"
        )
    )
    CALHAN = Municipality(
        name="Calhan",
        abbreviations=PlaceAbbreviations(
            three_letter="CLH",
            five_letter="CLHAN",
            seven_letter="CALHAN",
            fourteen_letter="CALHAN"
        )
    )
    CAMPO = Municipality(
        name="Campo",
        abbreviations=PlaceAbbreviations(
            three_letter="CMP",
            five_letter="CAMPO",
            seven_letter="CAMPO",
            fourteen_letter="CAMPO"
        )
    )
    CANON_CITY = Municipality(
        name="Cañon City",
        abbreviations=PlaceAbbreviations(
            three_letter="CNC",
            five_letter="CANON",
            seven_letter="CANCITY",
            fourteen_letter="CANONCITY"
        )
    )
    CARBONATE = Municipality(
        name="Carbonate",
        abbreviations=PlaceAbbreviations(
            three_letter="CRB",
            five_letter="CBNTE",
            seven_letter="CRBNATE",
            fourteen_letter="CARBONATE"
        )
    )
    CARBONDALE = Municipality(
        name="Carbondale",
        abbreviations=PlaceAbbreviations(
            three_letter="CRD",
            five_letter="CBNDL",
            seven_letter="CRBDALE",
            fourteen_letter="CARBONDALE"
        )
    )
    CASTLE_PINES = Municipality(
        name="Castle Pines",
        abbreviations=PlaceAbbreviations(
            three_letter="CSP",
            five_letter="CSTLP",
            seven_letter="CSTLPNS",
            fourteen_letter="CASTLEPINES"
        )
    )
    CASTLE_ROCK = Municipality(
        name="Castle Rock",
        abbreviations=PlaceAbbreviations(
            three_letter="CSR",
            five_letter="CSTLR",
            seven_letter="CSTLRCK",
            fourteen_letter="CASTLEROCK"
        )
    )
    CEDAREDGE = Municipality(
        name="Cedaredge",
        abbreviations=PlaceAbbreviations(
            three_letter="CDG",
            five_letter="CREDG",
            seven_letter="CDREDGE",
            fourteen_letter="CEDAREDGE"
        )
    )
    CENTENNIAL = Municipality(
        name="Centennial",
        abbreviations=PlaceAbbreviations(
            three_letter="CEN",
            five_letter="CENTL",
            seven_letter="CENTNNL",
            fourteen_letter="CENTENNIAL"
        )
    )
    CENTER = Municipality(
        name="Center",
        abbreviations=PlaceAbbreviations(
            three_letter="CTR",
            five_letter="CENTR",
            seven_letter="CENTER",
            fourteen_letter="CENTER"
        )
    )
    CENTRAL_CITY = Municipality(
        name="Central City",
        abbreviations=PlaceAbbreviations(
            three_letter="CCT",
            five_letter="CNTCY",
            seven_letter="CENCITY",
            fourteen_letter="CENTRALCITY"
        )
    )
    CHERAW = Municipality(
        name="Cheraw",
        abbreviations=PlaceAbbreviations(
            three_letter="CRW",
            five_letter="CHRAW",
            seven_letter="CHERAW",
            fourteen_letter="CHERAW"
        )
    )
    CHERRY_HILLS_VILLAGE = Municipality(
        name="Cherry Hills Village",
        abbreviations=PlaceAbbreviations(
            three_letter="CHV",
            five_letter="CHRVL",
            seven_letter="CHRVHLL",
            fourteen_letter="CHERRYHILLS"
        )
    )
    CHEYENNE_WELLS = Municipality(
        name="Cheyenne Wells",
        abbreviations=PlaceAbbreviations(
            three_letter="CHW",
            five_letter="CHYWL",
            seven_letter="CHYWLLS",
            fourteen_letter="CHEYENNEWELLS"
        )
    )
    COAL_CREEK = Municipality(
        name="Coal Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="CLC",
            five_letter="COALC",
            seven_letter="COALCRK",
            fourteen_letter="COALCREEK"
        )
    )
    COKEDALE = Municipality(
        name="Cokedale",
        abbreviations=PlaceAbbreviations(
            three_letter="CKD",
            five_letter="COKDL",
            seven_letter="COKEDAL",
            fourteen_letter="COKEDALE"
        )
    )
    COLLBRAN = Municipality(
        name="Collbran",
        abbreviations=PlaceAbbreviations(
            three_letter="CLB",
            five_letter="COLLB",
            seven_letter="COLLBRN",
            fourteen_letter="COLLBRAN"
        )
    )
    COLORADO_SPRINGS = Municipality(
        name="Colorado Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="COS",
            five_letter="CSPRG",
            seven_letter="COSPRGS",
            fourteen_letter="COSPRINGS"
        )
    )
    COLUMBINE_VALLEY = Municipality(
        name="Columbine Valley",
        abbreviations=PlaceAbbreviations(
            three_letter="CLV",
            five_letter="CLBVY",
            seven_letter="CLBNVLY",
            fourteen_letter="CLMBINE VALLEY"
        )
    )
    COMMERCE_CITY = Municipality(
        name="Commerce City",
        abbreviations=PlaceAbbreviations(
            three_letter="CMC",
            five_letter="CMRCE",
            seven_letter="COMCITY",
            fourteen_letter="COMMERCECITY"
        )
    )
    CORTEZ = Municipality(
        name="Cortez",
        abbreviations=PlaceAbbreviations(
            three_letter="CRZ",
            five_letter="CRTEZ",
            seven_letter="CORTEZ",
            fourteen_letter="CORTEZ"
        )
    )
    CRAIG = Municipality(
        name="Craig",
        abbreviations=PlaceAbbreviations(
            three_letter="CRG",
            five_letter="CRAIG",
            seven_letter="CRAIG",
            fourteen_letter="CRAIG"
        )
    )
    CRAWFORD = Municipality(
        name="Crawford",
        abbreviations=PlaceAbbreviations(
            three_letter="CRF",
            five_letter="CRWFD",
            seven_letter="CRWFORD",
            fourteen_letter="CRAWFORD"
        )
    )
    CREEDE = Municipality(
        name="Creede",
        abbreviations=PlaceAbbreviations(
            three_letter="CRD",
            five_letter="CREED",
            seven_letter="CREEDE",
            fourteen_letter="CREEDE"
        )
    )
    CRESTED_BUTTE = Municipality(
        name="Crested Butte",
        abbreviations=PlaceAbbreviations(
            three_letter="CRB",
            five_letter="CRSTB",
            seven_letter="CRSTBT",
            fourteen_letter="CRESTEDBUTTE"
        )
    )
    CRESTONE = Municipality(
        name="Crestone",
        abbreviations=PlaceAbbreviations(
            three_letter="CRS",
            five_letter="CRSTN",
            seven_letter="CRSTONE",
            fourteen_letter="CRESTONE"
        )
    )
    CRIPPLE_CREEK = Municipality(
        name="Cripple Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="CRP",
            five_letter="CRPLC",
            seven_letter="CRPLCRK",
            fourteen_letter="CRIPPLECREEK"
        )
    )
    CROOK = Municipality(
        name="Crook",
        abbreviations=PlaceAbbreviations(
            three_letter="CRK",
            five_letter="CROOK",
            seven_letter="CROOK",
            fourteen_letter="CROOK"
        )
    )
    CROWLEY = Municipality(
        name="Crowley",
        abbreviations=PlaceAbbreviations(
            three_letter="CRW",
            five_letter="CRWLY",
            seven_letter="CROWLEY",
            fourteen_letter="CROWLEY"
        )
    )
    DACONO = Municipality(
        name="Dacono",
        abbreviations=PlaceAbbreviations(
            three_letter="DAC",
            five_letter="DACNO",
            seven_letter="DACONO",
            fourteen_letter="DACONO"
        )
    )
    DE_BEQUE = Municipality(
        name="De Beque",
        abbreviations=PlaceAbbreviations(
            three_letter="DBQ",
            five_letter="DEBEQ",
            seven_letter="DEBEQUE",
            fourteen_letter="DEBEQUE"
        )
    )
    DEER_TRAIL = Municipality(
        name="Deer Trail",
        abbreviations=PlaceAbbreviations(
            three_letter="DRT",
            five_letter="DRTRL",
            seven_letter="DRTRAIL",
            fourteen_letter="DEERTRAIL"
        )
    )
    DEL_NORTE = Municipality(
        name="Del Norte",
        abbreviations=PlaceAbbreviations(
            three_letter="DLN",
            five_letter="DELNT",
            seven_letter="DELNORT",
            fourteen_letter="DELNORTE"
        )
    )
    DELTA = Municipality(
        name="Delta",
        abbreviations=PlaceAbbreviations(
            three_letter="DLT",
            five_letter="DELTA",
            seven_letter="DELTA",
            fourteen_letter="DELTA"
        )
    )
    DENVER = Municipality(
        name="Denver",
        abbreviations=PlaceAbbreviations(
            three_letter="DEN",
            five_letter="DENVR",
            seven_letter="DENVER",
            fourteen_letter="DENVER"
        )
    )
    DILLON = Municipality(
        name="Dillon",
        abbreviations=PlaceAbbreviations(
            three_letter="DLN",
            five_letter="DLLN",
            seven_letter="DILLON",
            fourteen_letter="DILLON"
        )
    )
    DINOSAUR = Municipality(
        name="Dinosaur",
        abbreviations=PlaceAbbreviations(
            three_letter="DNS",
            five_letter="DINOS",
            seven_letter="DINOSR",
            fourteen_letter="DINOSAUR"
        )
    )
    DOLORES = Municipality(
        name="Dolores",
        abbreviations=PlaceAbbreviations(
            three_letter="DLS",
            five_letter="DOLOS",
            seven_letter="DOLORES",
            fourteen_letter="DOLORES"
        )
    )
    DOVE_CREEK = Municipality(
        name="Dove Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="DVC",
            five_letter="DOVEC",
            seven_letter="DVCREEK",
            fourteen_letter="DOVECREEK"
        )
    )
    DURANGO = Municipality(
        name="Durango",
        abbreviations=PlaceAbbreviations(
            three_letter="DUR",
            five_letter="DURAN",
            seven_letter="DURANGO",
            fourteen_letter="DURANGO"
        )
    )
    EADS = Municipality(
        name="Eads",
        abbreviations=PlaceAbbreviations(
            three_letter="EAD",
            five_letter="EADS",
            seven_letter="EADS",
            fourteen_letter="EADS"
        )
    )
    EAGLE = Municipality(
        name="Eagle",
        abbreviations=PlaceAbbreviations(
            three_letter="EAG",
            five_letter="EAGLE",
            seven_letter="EAGLE",
            fourteen_letter="EAGLE"
        )
    )
    EATON = Municipality(
        name="Eaton",
        abbreviations=PlaceAbbreviations(
            three_letter="EAT",
            five_letter="EATON",
            seven_letter="EATON",
            fourteen_letter="EATON"
        )
    )
    ECKLEY = Municipality(
        name="Eckley",
        abbreviations=PlaceAbbreviations(
            three_letter="ECK",
            five_letter="ECKLY",
            seven_letter="ECKLEY",
            fourteen_letter="ECKLEY"
        )
    )
    EDGEWATER = Municipality(
        name="Edgewater",
        abbreviations=PlaceAbbreviations(
            three_letter="EDW",
            five_letter="EDGWT",
            seven_letter="EDGWATR",
            fourteen_letter="EDGEWATER"
        )
    )
    ELIZABETH = Municipality(
        name="Elizabeth",
        abbreviations=PlaceAbbreviations(
            three_letter="ELI",
            five_letter="ELIZB",
            seven_letter="ELZBETH",
            fourteen_letter="ELIZABETH"
        )
    )
    EMPIRE = Municipality(
        name="Empire",
        abbreviations=PlaceAbbreviations(
            three_letter="EMP",
            five_letter="EMPR",
            seven_letter="EMPIRE",
            fourteen_letter="EMPIRE"
        )
    )
    ENGLEWOOD = Municipality(
        name="Englewood",
        abbreviations=PlaceAbbreviations(
            three_letter="ENL",
            five_letter="ENGLW",
            seven_letter="ENGLWD",
            fourteen_letter="ENGLEWOOD"
        )
    )
    ERIE = Municipality(
        name="Erie",
        abbreviations=PlaceAbbreviations(
            three_letter="ERI",
            five_letter="ERIE",
            seven_letter="ERIE",
            fourteen_letter="ERIE"
        )
    )
    ESTES_PARK = Municipality(
        name="Estes Park",
        abbreviations=PlaceAbbreviations(
            three_letter="ESP",
            five_letter="ESTPK",
            seven_letter="ESTPARK",
            fourteen_letter="ESTESPARK"
        )
    )
    EVANS = Municipality(
        name="Evans",
        abbreviations=PlaceAbbreviations(
            three_letter="EVA",
            five_letter="EVANS",
            seven_letter="EVANS",
            fourteen_letter="EVANS"
        )
    )
    FAIRPLAY = Municipality(
        name="Fairplay",
        abbreviations=PlaceAbbreviations(
            three_letter="FPL",
            five_letter="FAIRP",
            seven_letter="FAIRPLY",
            fourteen_letter="FAIRPLAY"
        )
    )
    FEDERAL_HEIGHTS = Municipality(
        name="Federal Heights",
        abbreviations=PlaceAbbreviations(
            three_letter="FHE",
            five_letter="FEDHG",
            seven_letter="FEDHGTS",
            fourteen_letter="FEDHEIGHTS"
        )
    )
    FIRESTONE = Municipality(
        name="Firestone",
        abbreviations=PlaceAbbreviations(
            three_letter="FST",
            five_letter="FIRES",
            seven_letter="FIRESTN",
            fourteen_letter="FIRESTONE"
        )
    )
    FLAGLER = Municipality(
        name="Flagler",
        abbreviations=PlaceAbbreviations(
            three_letter="FLG",
            five_letter="FLAGL",
            seven_letter="FLAGLER",
            fourteen_letter="FLAGLER"
        )
    )
    FLEMING = Municipality(
        name="Fleming",
        abbreviations=PlaceAbbreviations(
            three_letter="FLM",
            five_letter="FLEMG",
            seven_letter="FLEMING",
            fourteen_letter="FLEMING"
        )
    )
    FLORENCE = Municipality(
        name="Florence",
        abbreviations=PlaceAbbreviations(
            three_letter="FLR",
            five_letter="FLRNC",
            seven_letter="FLOREN",
            fourteen_letter="FLORENCE"
        )
    )
    FORT_COLLINS = Municipality(
        name="Fort Collins",
        abbreviations=PlaceAbbreviations(
            three_letter="FCL",
            five_letter="FOCO",
            seven_letter="FORTCLL",
            fourteen_letter="FORTCOLLINS"
        )
    )
    FORT_LUPTON = Municipality(
        name="Fort Lupton",
        abbreviations=PlaceAbbreviations(
            three_letter="FLP",
            five_letter="FLUPT",
            seven_letter="FORTLUP",
            fourteen_letter="FORTLUPTON"
        )
    )
    FORT_MORGAN = Municipality(
        name="Fort Morgan",
        abbreviations=PlaceAbbreviations(
            three_letter="FMG",
            five_letter="FMORG",
            seven_letter="FORTMOR",
            fourteen_letter="FORTMORGAN"
        )
    )
    FOUNTAIN = Municipality(
        name="Fountain",
        abbreviations=PlaceAbbreviations(
            three_letter="FTN",
            five_letter="FOUNT",
            seven_letter="FOUNTN",
            fourteen_letter="FOUNTAIN"
        )
    )
    FOWLER = Municipality(
        name="Fowler",
        abbreviations=PlaceAbbreviations(
            three_letter="FOW",
            five_letter="FOWLR",
            seven_letter="FOWLER",
            fourteen_letter="FOWLER"
        )
    )
    FOXFIELD = Municipality(
        name="Foxfield",
        abbreviations=PlaceAbbreviations(
            three_letter="FXF",
            five_letter="FXFLD",
            seven_letter="FOXFLD",
            fourteen_letter="FOXFIELD"
        )
    )
    FRASER = Municipality(
        name="Fraser",
        abbreviations=PlaceAbbreviations(
            three_letter="FRS",
            five_letter="FRASR",
            seven_letter="FRASER",
            fourteen_letter="FRASER"
        )
    )
    FREDERICK = Municipality(
        name="Frederick",
        abbreviations=PlaceAbbreviations(
            three_letter="FRD",
            five_letter="FREDK",
            seven_letter="FREDRCK",
            fourteen_letter="FREDERICK"
        )
    )
    FRISCO = Municipality(
        name="Frisco",
        abbreviations=PlaceAbbreviations(
            three_letter="FRI",
            five_letter="FRSCO",
            seven_letter="FRISCO",
            fourteen_letter="FRISCO"
        )
    )
    FRUITA = Municipality(
        name="Fruita",
        abbreviations=PlaceAbbreviations(
            three_letter="FRU",
            five_letter="FRUIT",
            seven_letter="FRUITA",
            fourteen_letter="FRUITA"
        )
    )
    GARDEN_CITY = Municipality(
        name="Garden City",
        abbreviations=PlaceAbbreviations(
            three_letter="GDC",
            five_letter="GRDNC",
            seven_letter="GARDEN",
            fourteen_letter="GARDENCITY"
        )
    )
    GENOA = Municipality(
        name="Genoa",
        abbreviations=PlaceAbbreviations(
            three_letter="GNO",
            five_letter="GENOA",
            seven_letter="GENOA",
            fourteen_letter="GENOA"
        )
    )
    GEORGETOWN = Municipality(
        name="Georgetown",
        abbreviations=PlaceAbbreviations(
            three_letter="GEO",
            five_letter="GEORT",
            seven_letter="GEORGTN",
            fourteen_letter="GEORGETOWN"
        )
    )
    GILCREST = Municipality(
        name="Gilcrest",
        abbreviations=PlaceAbbreviations(
            three_letter="GLC",
            five_letter="GLCST",
            seven_letter="GILCRST",
            fourteen_letter="GILCREST"
        )
    )
    GLENDALE = Municipality(
        name="Glendale",
        abbreviations=PlaceAbbreviations(
            three_letter="GLN",
            five_letter="GLNDL",
            seven_letter="GLENDA",
            fourteen_letter="GLENDALE"
        )
    )
    GLENWOOD_SPRINGS = Municipality(
        name="Glenwood Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="GLW",
            five_letter="GLWDS",
            seven_letter="GWSPRGS",
            fourteen_letter="GLNWOODSPRINGS"
        )
    )
    GOLDEN = Municipality(
        name="Golden",
        abbreviations=PlaceAbbreviations(
            three_letter="GLD",
            five_letter="GLDN",
            seven_letter="GOLDEN",
            fourteen_letter="GOLDEN"
        )
    )
    GRANADA = Municipality(
        name="Granada",
        abbreviations=PlaceAbbreviations(
            three_letter="GRN",
            five_letter="GRNDA",
            seven_letter="GRANADA",
            fourteen_letter="GRANADA"
        )
    )
    GRANBY = Municipality(
        name="Granby",
        abbreviations=PlaceAbbreviations(
            three_letter="GRB",
            five_letter="GRNBY",
            seven_letter="GRANBY",
            fourteen_letter="GRANBY"
        )
    )
    GRAND_JUNCTION = Municipality(
        name="Grand Junction",
        abbreviations=PlaceAbbreviations(
            three_letter="GJT",
            five_letter="GRJCT",
            seven_letter="GRNDJCT",
            fourteen_letter="GRANDJUNCTION"
        )
    )
    GRAND_LAKE = Municipality(
        name="Grand Lake",
        abbreviations=PlaceAbbreviations(
            three_letter="GDL",
            five_letter="GRDLK",
            seven_letter="GRANDLK",
            fourteen_letter="GRANDLAKE"
        )
    )
    GREELEY = Municipality(
        name="Greeley",
        abbreviations=PlaceAbbreviations(
            three_letter="GRL",
            five_letter="GRELY",
            seven_letter="GREELY",
            fourteen_letter="GREELEY"
        )
    )
    GREEN_MOUNTAIN_FALLS = Municipality(
        name="Green Mountain Falls",
        abbreviations=PlaceAbbreviations(
            three_letter="GMF",
            five_letter="GRMNT",
            seven_letter="GRMTFLS",
            fourteen_letter="GREENMTNFALLS"
        )
    )
    GREENWOOD_VILLAGE = Municipality(
        name="Greenwood Village",
        abbreviations=PlaceAbbreviations(
            three_letter="GRV",
            five_letter="GRWDV",
            seven_letter="GRWDVL",
            fourteen_letter="GREENWOODVLG"
        )
    )
    GROVER = Municipality(
        name="Grover",
        abbreviations=PlaceAbbreviations(
            three_letter="GVR",
            five_letter="GROVR",
            seven_letter="GROVER",
            fourteen_letter="GROVER"
        )
    )
    GUNNISON = Municipality(
        name="Gunnison",
        abbreviations=PlaceAbbreviations(
            three_letter="GUN",
            five_letter="GUNN",
            seven_letter="GUNNISN",
            fourteen_letter="GUNNISON"
        )
    )
    GYPSUM = Municipality(
        name="Gypsum",
        abbreviations=PlaceAbbreviations(
            three_letter="GYP",
            five_letter="GYPSM",
            seven_letter="GYPSUM",
            fourteen_letter="GYPSUM"
        )
    )
    HARTMAN = Municipality(
        name="Hartman",
        abbreviations=PlaceAbbreviations(
            three_letter="HRT",
            five_letter="HRTMN",
            seven_letter="HARTMAN",
            fourteen_letter="HARTMAN"
        )
    )
    HAXTUN = Municipality(
        name="Haxtun",
        abbreviations=PlaceAbbreviations(
            three_letter="HAX",
            five_letter="HAXTN",
            seven_letter="HAXTUN",
            fourteen_letter="HAXTUN"
        )
    )
    HAYDEN = Municipality(
        name="Hayden",
        abbreviations=PlaceAbbreviations(
            three_letter="HAY",
            five_letter="HAYDN",
            seven_letter="HAYDEN",
            fourteen_letter="HAYDEN"
        )
    )
    HILLROSE = Municipality(
        name="Hillrose",
        abbreviations=PlaceAbbreviations(
            three_letter="HRS",
            five_letter="HILRS",
            seven_letter="HILLRS",
            fourteen_letter="HILLROSE"
        )
    )
    HOLLY = Municipality(
        name="Holly",
        abbreviations=PlaceAbbreviations(
            three_letter="HOL",
            five_letter="HOLLY",
            seven_letter="HOLLY",
            fourteen_letter="HOLLY"
        )
    )
    HOLYOKE = Municipality(
        name="Holyoke",
        abbreviations=PlaceAbbreviations(
            three_letter="HLY",
            five_letter="HOLYK",
            seven_letter="HOLYOKE",
            fourteen_letter="HOLYOKE"
        )
    )
    HOOPER = Municipality(
        name="Hooper",
        abbreviations=PlaceAbbreviations(
            three_letter="HPR",
            five_letter="HOOPR",
            seven_letter="HOOPER",
            fourteen_letter="HOOPER"
        )
    )
    HOT_SULPHER_SPRINGS = Municipality(
        name="Hot Sulphur Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="HSS",
            five_letter="HTSUL",
            seven_letter="HTSULP",
            fourteen_letter="HOTSLPSPRINGS"
        )
    )
    HOTCHKISS = Municipality(
        name="Hotchkiss",
        abbreviations=PlaceAbbreviations(
            three_letter="HCK",
            five_letter="HOTCK",
            seven_letter="HOTCHKS",
            fourteen_letter="HOTCHKISS"
        )
    )
    HUDSON = Municipality(
        name="Hudson",
        abbreviations=PlaceAbbreviations(
            three_letter="HDS",
            five_letter="HUDSN",
            seven_letter="HUDSON",
            fourteen_letter="HUDSON"
        )
    )
    HUGO = Municipality(
        name="Hugo",
        abbreviations=PlaceAbbreviations(
            three_letter="HUG",
            five_letter="HUGO",
            seven_letter="HUGO",
            fourteen_letter="HUGO"
        )
    )
    IDAHO_SPRINGS = Municipality(
        name="Idaho Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="IDS",
            five_letter="IDSPR",
            seven_letter="IDSPRGS",
            fourteen_letter="IDAHOSPRINGS"
        )
    )
    IGNACIO = Municipality(
        name="Ignacio",
        abbreviations=PlaceAbbreviations(
            three_letter="IGN",
            five_letter="IGNAC",
            seven_letter="IGNACIO",
            fourteen_letter="IGNACIO"
        )
    )
    ILIFF = Municipality(
        name="Iliff",
        abbreviations=PlaceAbbreviations(
            three_letter="ILF",
            five_letter="ILIFF",
            seven_letter="ILIFF",
            fourteen_letter="ILIFF"
        )
    )
    JAMESTOWN = Municipality(
        name="Jamestown",
        abbreviations=PlaceAbbreviations(
            three_letter="JAM",
            five_letter="JAMST",
            seven_letter="JAMESTN",
            fourteen_letter="JAMESTOWN"
        )
    )
    JOHNSTOWN = Municipality(
        name="Johnstown",
        abbreviations=PlaceAbbreviations(
            three_letter="JHN",
            five_letter="JOHNS",
            seven_letter="JOHNSTN",
            fourteen_letter="JOHNSTOWN"
        )
    )
    JULESBURG = Municipality(
        name="Julesburg",
        abbreviations=PlaceAbbreviations(
            three_letter="JUL",
            five_letter="JULSB",
            seven_letter="JULSBRG",
            fourteen_letter="JULESBURG"
        )
    )
    KEENESBURG = Municipality(
        name="Keenesburg",
        abbreviations=PlaceAbbreviations(
            three_letter="KNS",
            five_letter="KEENS",
            seven_letter="KEENSBG",
            fourteen_letter="KEENESBURG"
        )
    )
    KERSEY = Municipality(
        name="Kersey",
        abbreviations=PlaceAbbreviations(
            three_letter="KRS",
            five_letter="KERSY",
            seven_letter="KERSEY",
            fourteen_letter="KERSEY"
        )
    )
    KEYSTONE = Municipality(
        name="Keystone",
        abbreviations=PlaceAbbreviations(
            three_letter="KYS",
            five_letter="KEYST",
            seven_letter="KEYSTN",
            fourteen_letter="KEYSTONE"
        )
    )
    KIM = Municipality(
        name="Kim",
        abbreviations=PlaceAbbreviations(
            three_letter="KIM",
            five_letter="KIM",
            seven_letter="KIM",
            fourteen_letter="KIM"
        )
    )
    KIOWA = Municipality(
        name="Kiowa",
        abbreviations=PlaceAbbreviations(
            three_letter="KIW",
            five_letter="KIOWA",
            seven_letter="KIOWA",
            fourteen_letter="KIOWA"
        )
    )
    KIT_CARSON = Municipality(
        name="Kit Carson",
        abbreviations=PlaceAbbreviations(
            three_letter="KIT",
            five_letter="KITCR",
            seven_letter="KITCRSN",
            fourteen_letter="KITCARSON"
        )
    )
    KREMMLING = Municipality(
        name="Kremmling",
        abbreviations=PlaceAbbreviations(
            three_letter="KRM",
            five_letter="KRMML",
            seven_letter="KRMMLNG",
            fourteen_letter="KREMMLING"
        )
    )
    LA_JARA = Municipality(
        name="La Jara",
        abbreviations=PlaceAbbreviations(
            three_letter="LJR",
            five_letter="LAJRA",
            seven_letter="LAJARA",
            fourteen_letter="LAJARA"
        )
    )
    LA_JUNTA = Municipality(
        name="La Junta",
        abbreviations=PlaceAbbreviations(
            three_letter="LJT",
            five_letter="LAJUN",
            seven_letter="LAJUNTA",
            fourteen_letter="LAJUNTA"
        )
    )
    LA_VETA = Municipality(
        name="La Veta",
        abbreviations=PlaceAbbreviations(
            three_letter="LVT",
            five_letter="LAVTA",
            seven_letter="LAVETA",
            fourteen_letter="LAVETA"
        )
    )
    LAFAYETTE = Municipality(
        name="Lafayette",
        abbreviations=PlaceAbbreviations(
            three_letter="LAF",
            five_letter="LFYTE",
            seven_letter="LFAYTE",
            fourteen_letter="LAFAYETTE"
        )
    )
    LAKE_CITY = Municipality(
        name="Lake City",
        abbreviations=PlaceAbbreviations(
            three_letter="LKC",
            five_letter="LKCTY",
            seven_letter="LKCITY",
            fourteen_letter="LAKECITY"
        )
    )
    LAKESIDE = Municipality(
        name="Lakeside",
        abbreviations=PlaceAbbreviations(
            three_letter="LKS",
            five_letter="LAKSD",
            seven_letter="LAKSIDE",
            fourteen_letter="LAKESIDE"
        )
    )
    LAKEWOOD = Municipality(
        name="Lakewood",
        abbreviations=PlaceAbbreviations(
            three_letter="LKW",
            five_letter="LAKWD",
            seven_letter="LKWOOD",
            fourteen_letter="LAKEWOOD"
        )
    )
    LAMAR = Municipality(
        name="Lamar",
        abbreviations=PlaceAbbreviations(
            three_letter="LMR",
            five_letter="LAMAR",
            seven_letter="LAMAR",
            fourteen_letter="LAMAR"
        )
    )
    LARKSPUR = Municipality(
        name="Larkspur",
        abbreviations=PlaceAbbreviations(
            three_letter="LRK",
            five_letter="LRKSP",
            seven_letter="LRKSPR",
            fourteen_letter="LARKSPUR"
        )
    )
    LAS_ANIMAS = Municipality(
        name="Las Animas",
        abbreviations=PlaceAbbreviations(
            three_letter="LAS",
            five_letter="LSANM",
            seven_letter="LSANMAS",
            fourteen_letter="LASANIMAS"
        )
    )
    LASALLE = Municipality(
        name="LaSalle",
        abbreviations=PlaceAbbreviations(
            three_letter="LSL",
            five_letter="LASLL",
            seven_letter="LASALLE",
            fourteen_letter="LASALLE"
        )
    )
    LEADVILLE = Municipality(
        name="Leadville",
        abbreviations=PlaceAbbreviations(
            three_letter="LDV",
            five_letter="LEADV",
            seven_letter="LEADVLL",
            fourteen_letter="LEADVILLE"
        )
    )
    LIMON = Municipality(
        name="Limon",
        abbreviations=PlaceAbbreviations(
            three_letter="LMN",
            five_letter="LIMON",
            seven_letter="LIMON",
            fourteen_letter="LIMON"
        )
    )
    LITTLETON = Municipality(
        name="Littleton",
        abbreviations=PlaceAbbreviations(
            three_letter="LIT",
            five_letter="LTTN",
            seven_letter="LTTN",
            fourteen_letter="LITTLETON"
        )
    )
    LOCHBUIE = Municipality(
        name="Lochbuie",
        abbreviations=PlaceAbbreviations(
            three_letter="LCB",
            five_letter="LOCHB",
            seven_letter="LOCHBUI",
            fourteen_letter="LOCHBUIE"
        )
    )
    LOG_LANE_VILLAGE = Municipality(
        name="Log Lane Village",
        abbreviations=PlaceAbbreviations(
            three_letter="LLV",
            five_letter="LOGLV",
            seven_letter="LOGLNVL",
            fourteen_letter="LOGLANEVLG"
        )
    )
    LONE_TREE = Municipality(
        name="Lone Tree",
        abbreviations=PlaceAbbreviations(
            three_letter="LNT",
            five_letter="LNTRE",
            seven_letter="LNTREE",
            fourteen_letter="LONETREE"
        )
    )
    LONGMONT = Municipality(
        name="Longmont",
        abbreviations=PlaceAbbreviations(
            three_letter="LGM",
            five_letter="LONGM",
            seven_letter="LONGMT",
            fourteen_letter="LONGMONT"
        )
    )
    LOUISVILLE = Municipality(
        name="Louisville",
        abbreviations=PlaceAbbreviations(
            three_letter="LOU",
            five_letter="LSVL",
            seven_letter="LSVL",
            fourteen_letter="LOUISVILLE"
        )
    )
    LOVELAND = Municipality(
        name="Loveland",
        abbreviations=PlaceAbbreviations(
            three_letter="LOV",
            five_letter="LOVE",
            seven_letter="LOVELD",
            fourteen_letter="LOVELAND"
        )
    )
    LYONS = Municipality(
        name="Lyons",
        abbreviations=PlaceAbbreviations(
            three_letter="LYO",
            five_letter="LYONS",
            seven_letter="LYONS",
            fourteen_letter="LYONS"
        )
    )
    MANASSA = Municipality(
        name="Manassa",
        abbreviations=PlaceAbbreviations(
            three_letter="MNS",
            five_letter="MANSS",
            seven_letter="MANASSA",
            fourteen_letter="MANASSA"
        )
    )
    MANCOS = Municipality(
        name="Mancos",
        abbreviations=PlaceAbbreviations(
            three_letter="MNC",
            five_letter="MANC",
            seven_letter="MANCOS",
            fourteen_letter="MANCOS"
        )
    )
    MANITOU_SPRINGS = Municipality(
        name="Manitou Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="MNS",
            five_letter="MSPRG",
            seven_letter="MNSPRGS",
            fourteen_letter="MANITOUSPRINGS"
        )
    )
    MANZANOLA = Municipality(
        name="Manzanola",
        abbreviations=PlaceAbbreviations(
            three_letter="MZL",
            five_letter="MZLNA",
            seven_letter="MANZANL",
            fourteen_letter="MANZANOLA"
        )
    )
    MARBLE = Municipality(
        name="Marble",
        abbreviations=PlaceAbbreviations(
            three_letter="MRB",
            five_letter="MARBL",
            seven_letter="MARBLE",
            fourteen_letter="MARBLE"
        )
    )
    MEAD = Municipality(
        name="Mead",
        abbreviations=PlaceAbbreviations(
            three_letter="MED",
            five_letter="MEAD",
            seven_letter="MEAD",
            fourteen_letter="MEAD"
        )
    )
    MEEKER = Municipality(
        name="Meeker",
        abbreviations=PlaceAbbreviations(
            three_letter="MKR",
            five_letter="MEEKR",
            seven_letter="MEEKER",
            fourteen_letter="MEEKER"
        )
    )
    MERINO = Municipality(
        name="Merino",
        abbreviations=PlaceAbbreviations(
            three_letter="MRN",
            five_letter="MRINO",
            seven_letter="MERINO",
            fourteen_letter="MERINO"
        )
    )
    MILLIKEN = Municipality(
        name="Milliken",
        abbreviations=PlaceAbbreviations(
            three_letter="MLK",
            five_letter="MILKN",
            seven_letter="MLLIKEN",
            fourteen_letter="MILLIKEN"
        )
    )
    MINTURN = Municipality(
        name="Minturn",
        abbreviations=PlaceAbbreviations(
            three_letter="MTR",
            five_letter="MNTUR",
            seven_letter="MINTURN",
            fourteen_letter="MINTURN"
        )
    )
    MOFFAT = Municipality(
        name="Moffat",
        abbreviations=PlaceAbbreviations(
            three_letter="MOF",
            five_letter="MFFT",
            seven_letter="MOFFAT",
            fourteen_letter="MOFFAT"
        )
    )
    MONTE_VISTA = Municipality(
        name="Monte Vista",
        abbreviations=PlaceAbbreviations(
            three_letter="MTV",
            five_letter="MNVST",
            seven_letter="MNVISTA",
            fourteen_letter="MONTEVISTA"
        )
    )
    MONTEZUMA = Municipality(
        name="Montezuma",
        abbreviations=PlaceAbbreviations(
            three_letter="MTZ",
            five_letter="MNZMA",
            seven_letter="MNTZUMA",
            fourteen_letter="MONTEZUMA"
        )
    )
    MONTROSE = Municipality(
        name="Montrose",
        abbreviations=PlaceAbbreviations(
            three_letter="MTR",
            five_letter="MNTRO",
            seven_letter="MONTRSE",
            fourteen_letter="MONTROSE"
        )
    )
    MONUMENT = Municipality(
        name="Monument",
        abbreviations=PlaceAbbreviations(
            three_letter="MNM",
            five_letter="MNMT",
            seven_letter="MONUMT",
            fourteen_letter="MONUMENT"
        )
    )
    MORRISON = Municipality(
        name="Morrison",
        abbreviations=PlaceAbbreviations(
            three_letter="MRN",
            five_letter="MORRN",
            seven_letter="MORRSON",
            fourteen_letter="MORRISON"
        )
    )
    MOUNT_CRESTED_BUTTE = Municipality(
        name="Mount Crested Butte",
        abbreviations=PlaceAbbreviations(
            three_letter="MCB",
            five_letter="MTCB",
            seven_letter="MTCSTBT",
            fourteen_letter="MTCRESTEDBUTTE"
        )
    )
    MOUNTAIN_VIEW = Municipality(
        name="Mountain View",
        abbreviations=PlaceAbbreviations(
            three_letter="MVW",
            five_letter="MTNVW",
            seven_letter="MTNVIEW",
            fourteen_letter="MOUNTAINVIEW"
        )
    )
    MOUNTAIN_VILLAGE = Municipality(
        name="Mountain Village",
        abbreviations=PlaceAbbreviations(
            three_letter="MVL",
            five_letter="MTNVL",
            seven_letter="MTNVILL",
            fourteen_letter="MOUNTAINVLGE"
        )
    )
    NATURITA = Municipality(
        name="Naturita",
        abbreviations=PlaceAbbreviations(
            three_letter="NAT",
            five_letter="NATUR",
            seven_letter="NATURT",
            fourteen_letter="NATURITA"
        )
    )
    NEDERLAND = Municipality(
        name="Nederland",
        abbreviations=PlaceAbbreviations(
            three_letter="NED",
            five_letter="NEDER",
            seven_letter="NEDERL",
            fourteen_letter="NEDERLAND"
        )
    )
    NEW_CASTLE = Municipality(
        name="New Castle",
        abbreviations=PlaceAbbreviations(
            three_letter="NWC",
            five_letter="NEWCL",
            seven_letter="NEWCSTL",
            fourteen_letter="NEWCASTLE"
        )
    )
    NORTHGLENN = Municipality(
        name="Northglenn",
        abbreviations=PlaceAbbreviations(
            three_letter="NGL",
            five_letter="NGLEN",
            seven_letter="NGLENN",
            fourteen_letter="NORTHGLENN"
        )
    )
    NORWOOD = Municipality(
        name="Norwood",
        abbreviations=PlaceAbbreviations(
            three_letter="NRW",
            five_letter="NORWD",
            seven_letter="NORWOOD",
            fourteen_letter="NORWOOD"
        )
    )
    NUCLA = Municipality(
        name="Nucla",
        abbreviations=PlaceAbbreviations(
            three_letter="NUC",
            five_letter="NUCLA",
            seven_letter="NUCLA",
            fourteen_letter="NUCLA"
        )
    )
    NUNN = Municipality(
        name="Nunn",
        abbreviations=PlaceAbbreviations(
            three_letter="NUN",
            five_letter="NUNN",
            seven_letter="NUNN",
            fourteen_letter="NUNN"
        )
    )
    OAK_CREEK = Municipality(
        name="Oak Creek",
        abbreviations=PlaceAbbreviations(
            three_letter="OKC",
            five_letter="OAKCR",
            seven_letter="OAKCRK",
            fourteen_letter="OAKCREEK"
        )
    )
    OLATHE = Municipality(
        name="Olathe",
        abbreviations=PlaceAbbreviations(
            three_letter="OLT",
            five_letter="OLATH",
            seven_letter="OLATHE",
            fourteen_letter="OLATHE"
        )
    )
    OLNEY_SPRINGS = Municipality(
        name="Olney Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="OLS",
            five_letter="OLNSP",
            seven_letter="OLNSPRG",
            fourteen_letter="OLNEYSPRINGS"
        )
    )
    OPHIR = Municipality(
        name="Ophir",
        abbreviations=PlaceAbbreviations(
            three_letter="OPH",
            five_letter="OPHIR",
            seven_letter="OPHIR",
            fourteen_letter="OPHIR"
        )
    )
    ORCHARD_CITY = Municipality(
        name="Orchard City",
        abbreviations=PlaceAbbreviations(
            three_letter="ORC",
            five_letter="ORCHD",
            seven_letter="ORCHCTY",
            fourteen_letter="ORCHARDCITY"
        )
    )
    ORDWAY = Municipality(
        name="Ordway",
        abbreviations=PlaceAbbreviations(
            three_letter="ORD",
            five_letter="ORDWY",
            seven_letter="ORDWAY",
            fourteen_letter="ORDWAY"
        )
    )
    OTIS = Municipality(
        name="Otis",
        abbreviations=PlaceAbbreviations(
            three_letter="OTI",
            five_letter="OTIS",
            seven_letter="OTIS",
            fourteen_letter="OTIS"
        )
    )
    OURAY = Municipality(
        name="Ouray",
        abbreviations=PlaceAbbreviations(
            three_letter="OUR",
            five_letter="OURAY",
            seven_letter="OURAY",
            fourteen_letter="OURAY"
        )
    )
    OVID = Municipality(
        name="Ovid",
        abbreviations=PlaceAbbreviations(
            three_letter="OVI",
            five_letter="OVID",
            seven_letter="OVID",
            fourteen_letter="OVID"
        )
    )
    PAGOSA_SPRINGS = Municipality(
        name="Pagosa Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="PGS",
            five_letter="PGSAS",
            seven_letter="PAGOSAS",
            fourteen_letter="PAGOSASPRINGS"
        )
    )
    PALISADE = Municipality(
        name="Palisade",
        abbreviations=PlaceAbbreviations(
            three_letter="PLS",
            five_letter="PALIS",
            seven_letter="PALISD",
            fourteen_letter="PALISADE"
        )
    )
    PALMER_LAKE = Municipality(
        name="Palmer Lake",
        abbreviations=PlaceAbbreviations(
            three_letter="PML",
            five_letter="PALML",
            seven_letter="PALMLK",
            fourteen_letter="PALMERLAKE"
        )
    )
    PAOLI = Municipality(
        name="Paoli",
        abbreviations=PlaceAbbreviations(
            three_letter="PLI",
            five_letter="PAOLI",
            seven_letter="PAOLI",
            fourteen_letter="PAOLI"
        )
    )
    PAONIA = Municipality(
        name="Paonia",
        abbreviations=PlaceAbbreviations(
            three_letter="PAN",
            five_letter="PAONI",
            seven_letter="PAONIA",
            fourteen_letter="PAONIA"
        )
    )
    PARACHUTE = Municipality(
        name="Parachute",
        abbreviations=PlaceAbbreviations(
            three_letter="PRC",
            five_letter="PRCHT",
            seven_letter="PRCHUTE",
            fourteen_letter="PARACHUTE"
        )
    )
    PARKER = Municipality(
        name="Parker",
        abbreviations=PlaceAbbreviations(
            three_letter="PRK",
            five_letter="PARKR",
            seven_letter="PARKER",
            fourteen_letter="PARKER"
        )
    )
    PEETZ = Municipality(
        name="Peetz",
        abbreviations=PlaceAbbreviations(
            three_letter="PTZ",
            five_letter="PEETZ",
            seven_letter="PEETZ",
            fourteen_letter="PEETZ"
        )
    )
    PIERCE = Municipality(
        name="Pierce",
        abbreviations=PlaceAbbreviations(
            three_letter="PIR",
            five_letter="PIERC",
            seven_letter="PIERCE",
            fourteen_letter="PIERCE"
        )
    )
    PITKIN = Municipality(
        name="Pitkin",
        abbreviations=PlaceAbbreviations(
            three_letter="PIT",
            five_letter="PITKN",
            seven_letter="PITKIN",
            fourteen_letter="PITKIN"
        )
    )
    PLATTEVILLE = Municipality(
        name="Platteville",
        abbreviations=PlaceAbbreviations(
            three_letter="PLV",
            five_letter="PLTVL",
            seven_letter="PLTVLE",
            fourteen_letter="PLATTEVILLE"
        )
    )
    PONCHA_SPRINGS = Municipality(
        name="Poncha Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="PCS",
            five_letter="PCHAS",
            seven_letter="PONCHAS",
            fourteen_letter="PONCHASPRINGS"
        )
    )
    PRITCHETT = Municipality(
        name="Pritchett",
        abbreviations=PlaceAbbreviations(
            three_letter="PRT",
            five_letter="PRTCH",
            seven_letter="PRITCTT",
            fourteen_letter="PRITCHETT"
        )
    )
    PUEBLO = Municipality(
        name="Pueblo",
        abbreviations=PlaceAbbreviations(
            three_letter="PUB",
            five_letter="PUEBL",
            seven_letter="PUEBLO",
            fourteen_letter="PUEBLO"
        )
    )
    RAMAH = Municipality(
        name="Ramah",
        abbreviations=PlaceAbbreviations(
            three_letter="RMA",
            five_letter="RAMAH",
            seven_letter="RAMAH",
            fourteen_letter="RAMAH"
        )
    )
    RANGELY = Municipality(
        name="Rangely",
        abbreviations=PlaceAbbreviations(
            three_letter="RAN",
            five_letter="RANGL",
            seven_letter="RANGLY",
            fourteen_letter="RANGELY"
        )
    )
    RAYMER = Municipality(
        name="Raymer",
        abbreviations=PlaceAbbreviations(
            three_letter="RYM",
            five_letter="RAYMR",
            seven_letter="RAYMER",
            fourteen_letter="RAYMER"
        )
    )
    RED_CLIFF = Municipality(
        name="Red Cliff",
        abbreviations=PlaceAbbreviations(
            three_letter="RCL",
            five_letter="RCLIF",
            seven_letter="REDCLFF",
            fourteen_letter="REDCLIFF"
        )
    )
    RICO = Municipality(
        name="Rico",
        abbreviations=PlaceAbbreviations(
            three_letter="RIC",
            five_letter="RICO",
            seven_letter="RICO",
            fourteen_letter="RICO"
        )
    )
    RIDGWAY = Municipality(
        name="Ridgway",
        abbreviations=PlaceAbbreviations(
            three_letter="RDG",
            five_letter="RIDGW",
            seven_letter="RIDGWAY",
            fourteen_letter="RIDGWAY"
        )
    )
    RIFLE = Municipality(
        name="Rifle",
        abbreviations=PlaceAbbreviations(
            three_letter="RIF",
            five_letter="RIFLE",
            seven_letter="RIFLE",
            fourteen_letter="RIFLE"
        )
    )
    ROCKVALE = Municipality(
        name="Rockvale",
        abbreviations=PlaceAbbreviations(
            three_letter="RKV",
            five_letter="ROCKV",
            seven_letter="ROCKVL",
            fourteen_letter="ROCKVALE"
        )
    )
    ROCKY_FORD = Municipality(
        name="Rocky Ford",
        abbreviations=PlaceAbbreviations(
            three_letter="RKF",
            five_letter="ROCKF",
            seven_letter="ROCKYFD",
            fourteen_letter="ROCKYFORD"
        )
    )
    ROMEO = Municipality(
        name="Romeo",
        abbreviations=PlaceAbbreviations(
            three_letter="RMO",
            five_letter="ROMEO",
            seven_letter="ROMEO",
            fourteen_letter="ROMEO"
        )
    )
    RYE = Municipality(
        name="Rye",
        abbreviations=PlaceAbbreviations(
            three_letter="RYE",
            five_letter="RYE",
            seven_letter="RYE",
            fourteen_letter="RYE"
        )
    )
    SAGUACHE = Municipality(
        name="Saguache",
        abbreviations=PlaceAbbreviations(
            three_letter="SGC",
            five_letter="SAGCH",
            seven_letter="SAGCHE",
            fourteen_letter="SAGUACHE"
        )
    )
    SALIDA = Municipality(
        name="Salida",
        abbreviations=PlaceAbbreviations(
            three_letter="SLD",
            five_letter="SALID",
            seven_letter="SALIDA",
            fourteen_letter="SALIDA"
        )
    )
    SAN_LUIS = Municipality(
        name="San Luis",
        abbreviations=PlaceAbbreviations(
            three_letter="SLS",
            five_letter="SLUIS",
            seven_letter="SANLUIS",
            fourteen_letter="SANLUIS"
        )
    )
    SANFORD = Municipality(
        name="Sanford",
        abbreviations=PlaceAbbreviations(
            three_letter="SFD",
            five_letter="SFORD",
            seven_letter="SANFORD",
            fourteen_letter="SANFORD"
        )
    )
    SAWPIT = Municipality(
        name="Sawpit",
        abbreviations=PlaceAbbreviations(
            three_letter="SAW",
            five_letter="SAWPT",
            seven_letter="SAWPIT",
            fourteen_letter="SAWPIT"
        )
    )
    SEDGWICK = Municipality(
        name="Sedgwick",
        abbreviations=PlaceAbbreviations(
            three_letter="SDW",
            five_letter="SEDGW",
            seven_letter="SEDGWCK",
            fourteen_letter="SEDGWICK"
        )
    )
    SEIBERT = Municipality(
        name="Seibert",
        abbreviations=PlaceAbbreviations(
            three_letter="SBT",
            five_letter="SBERT",
            seven_letter="SEIBERT",
            fourteen_letter="SEIBERT"
        )
    )
    SEVERANCE = Municipality(
        name="Severance",
        abbreviations=PlaceAbbreviations(
            three_letter="SVR",
            five_letter="SEVRN",
            seven_letter="SEVRNC",
            fourteen_letter="SEVERANCE"
        )
    )
    SHERIDAN = Municipality(
        name="Sheridan",
        abbreviations=PlaceAbbreviations(
            three_letter="SHR",
            five_letter="SHERD",
            seven_letter="SHERID",
            fourteen_letter="SHERIDAN"
        )
    )
    SHERIDAN_LAKE = Municipality(
        name="Sheridan Lake",
        abbreviations=PlaceAbbreviations(
            three_letter="SHL",
            five_letter="SHERL",
            seven_letter="SHERLK",
            fourteen_letter="SHERIDLAKE"
        )
    )
    SILT = Municipality(
        name="Silt",
        abbreviations=PlaceAbbreviations(
            three_letter="SLT",
            five_letter="SILT",
            seven_letter="SILT",
            fourteen_letter="SILT"
        )
    )
    SILVER_CLIFF = Municipality(
        name="Silver Cliff",
        abbreviations=PlaceAbbreviations(
            three_letter="SVC",
            five_letter="SVCLF",
            seven_letter="SVCLFF",
            fourteen_letter="SILVERCLIFF"
        )
    )
    SILVER_PLUME = Municipality(
        name="Silver Plume",
        abbreviations=PlaceAbbreviations(
            three_letter="SVP",
            five_letter="SVPLM",
            seven_letter="SVPLME",
            fourteen_letter="SILVERPLUME"
        )
    )
    SILVERTHORNE = Municipality(
        name="Silverthorne",
        abbreviations=PlaceAbbreviations(
            three_letter="SVT",
            five_letter="SVTHR",
            seven_letter="SVTHRN",
            fourteen_letter="SILVERTHORNE"
        )
    )
    SILVERTON = Municipality(
        name="Silverton",
        abbreviations=PlaceAbbreviations(
            three_letter="SVN",
            five_letter="SVLVT",
            seven_letter="SVLTON",
            fourteen_letter="SILVERTON"
        )
    )
    SILMA = Municipality(
        name="Simla",
        abbreviations=PlaceAbbreviations(
            three_letter="SIL",
            five_letter="SILMA",
            seven_letter="SILMA",
            fourteen_letter="SIMLA"
        )
    )
    SNOWMASS_VILLAGE = Municipality(
        name="Snowmass Village",
        abbreviations=PlaceAbbreviations(
            three_letter="SMV",
            five_letter="SNMVS",
            seven_letter="SNMVLLG",
            fourteen_letter="SNOWMASSVLG"
        )
    )
    SOUTH_FORK = Municipality(
        name="South Fork",
        abbreviations=PlaceAbbreviations(
            three_letter="SFK",
            five_letter="SFORK",
            seven_letter="SOUTHFK",
            fourteen_letter="SOUTHFORK"
        )
    )
    SPRINGFIELD = Municipality(
        name="Springfield",
        abbreviations=PlaceAbbreviations(
            three_letter="SPF",
            five_letter="SPRGF",
            seven_letter="SPRGFD",
            fourteen_letter="SPRINGFIELD"
        )
    )
    STARKVILLE = Municipality(
        name="Starkville",
        abbreviations=PlaceAbbreviations(
            three_letter="SKV",
            five_letter="STARK",
            seven_letter="STARKVL",
            fourteen_letter="STARKVILLE"
        )
    )
    STEAMBOAT_SPRINGS = Municipality(
        name="Steamboat Springs",
        abbreviations=PlaceAbbreviations(
            three_letter="STB",
            five_letter="STEAM",
            seven_letter="STMBOAT",
            fourteen_letter="STEAMBOATSPRGS"
        )
    )
    STERLING = Municipality(
        name="Sterling",
        abbreviations=PlaceAbbreviations(
            three_letter="STL",
            five_letter="STERL",
            seven_letter="STERLN",
            fourteen_letter="STERLING"
        )
    )
    STRATTON = Municipality(
        name="Stratton",
        abbreviations=PlaceAbbreviations(
            three_letter="STT",
            five_letter="STRAT",
            seven_letter="STRATN",
            fourteen_letter="STRATTON"
        )
    )
    SUGAR_CITY = Municipality(
        name="Sugar City",
        abbreviations=PlaceAbbreviations(
            three_letter="SGC",
            five_letter="SUGAR",
            seven_letter="SGRCITY",
            fourteen_letter="SUGARCITY"
        )
    )
    SUPERIOR = Municipality(
        name="Superior",
        abbreviations=PlaceAbbreviations(
            three_letter="SUP",
            five_letter="SUPER",
            seven_letter="SUPRIOR",
            fourteen_letter="SUPERIOR"
        )
    )
    SWINK = Municipality(
        name="Swink",
        abbreviations=PlaceAbbreviations(
            three_letter="SWK",
            five_letter="SWINK",
            seven_letter="SWINK",
            fourteen_letter="SWINK"
        )
    )
    TELLURIDE = Municipality(
        name="Telluride",
        abbreviations=PlaceAbbreviations(
            three_letter="TEL",
            five_letter="TELLR",
            seven_letter="TELLUR",
            fourteen_letter="TELLURIDE"
        )
    )
    THORNTON = Municipality(
        name="Thornton",
        abbreviations=PlaceAbbreviations(
            three_letter="THO",
            five_letter="THRTN",
            seven_letter="THRTON",
            fourteen_letter="THORNTON"
        )
    )
    TINMATH = Municipality(
        name="Tinmath",
        abbreviations=PlaceAbbreviations(
            three_letter="TIN",
            five_letter="TINMT",
            seven_letter="TINMATH",
            fourteen_letter="TINMATH"
        )
    )
    TRINIDAD = Municipality(
        name="Trinidad",
        abbreviations=PlaceAbbreviations(
            three_letter="TRI",
            five_letter="TRIND",
            seven_letter="TRINDD",
            fourteen_letter="TRINIDAD"
        )
    )
    TWO_BUTTES = Municipality(
        name="Two Buttes",
        abbreviations=PlaceAbbreviations(
            three_letter="TWB",
            five_letter="TWOBT",
            seven_letter="TWOBTTE",
            fourteen_letter="TWOBUTTES"
        )
    )
    VAIL = Municipality(
        name="Vail",
        abbreviations=PlaceAbbreviations(
            three_letter="VAI",
            five_letter="VAIL",
            seven_letter="VAIL",
            fourteen_letter="VAIL"
        )
    )
    VICTOR = Municipality(
        name="Victor",
        abbreviations=PlaceAbbreviations(
            three_letter="VIC",
            five_letter="VICTR",
            seven_letter="VICTOR",
            fourteen_letter="VICTOR"
        )
    )
    VILAS = Municipality(
        name="Vilas",
        abbreviations=PlaceAbbreviations(
            three_letter="VLS",
            five_letter="VILAS",
            seven_letter="VILAS",
            fourteen_letter="VILAS"
        )
    )
    VONA = Municipality(
        name="Vona",
        abbreviations=PlaceAbbreviations(
            three_letter="VON",
            five_letter="VONA",
            seven_letter="VONA",
            fourteen_letter="VONA"
        )
    )
    WALDEN = Municipality(
        name="Walden",
        abbreviations=PlaceAbbreviations(
            three_letter="WLD",
            five_letter="WALDN",
            seven_letter="WALDEN",
            fourteen_letter="WALDEN"
        )
    )
    WALSENBURG = Municipality(
        name="Walsenburg",
        abbreviations=PlaceAbbreviations(
            three_letter="WLB",
            five_letter="WALSN",
            seven_letter="WALSNB",
            fourteen_letter="WALSENBURG"
        )
    )
    WALSH = Municipality(
        name="Walsh",
        abbreviations=PlaceAbbreviations(
            three_letter="WLS",
            five_letter="WALSH",
            seven_letter="WALSH",
            fourteen_letter="WALSH"
        )
    )
    WARD = Municipality(
        name="Ward",
        abbreviations=PlaceAbbreviations(
            three_letter="WRD",
            five_letter="WARD",
            seven_letter="WARD",
            fourteen_letter="WARD"
        )
    )
    WELLINGTON = Municipality(
        name="Wellington",
        abbreviations=PlaceAbbreviations(
            three_letter="WEL",
            five_letter="WELLN",
            seven_letter="WELLGTN",
            fourteen_letter="WELLINGTON"
        )
    )
    WESTCLIFFE = Municipality(
        name="Westcliffe",
        abbreviations=PlaceAbbreviations(
            three_letter="WCL",
            five_letter="WCLFF",
            seven_letter="WESTCLF",
            fourteen_letter="WESTCLIFFE"
        )
    )
    WESTMINSTER = Municipality(
        name="Westminster",
        abbreviations=PlaceAbbreviations(
            three_letter="WMS",
            five_letter="WSTMR",
            seven_letter="WSTMNR",
            fourteen_letter="WESTMINSTER"
        )
    )
    WHEAT_RIDGE = Municipality(
        name="Wheat Ridge",
        abbreviations=PlaceAbbreviations(
            three_letter="WHR",
            five_letter="WHTRG",
            seven_letter="WHTRDGE",
            fourteen_letter="WHEATRIDGE"
        )
    )
    WIGGINS = Municipality(
        name="Wiggins",
        abbreviations=PlaceAbbreviations(
            three_letter="WIG",
            five_letter="WGGNS",
            seven_letter="WIGGINS",
            fourteen_letter="WIGGINS"
        )
    )
    WILEY = Municipality(
        name="Wiley",
        abbreviations=PlaceAbbreviations(
            three_letter="WLY",
            five_letter="WILEY",
            seven_letter="WILEY",
            fourteen_letter="WILEY"
        )
    )
    WILLIAMSBURG = Municipality(
        name="Williamsburg",
        abbreviations=PlaceAbbreviations(
            three_letter="WSB",
            five_letter="WMSBG",
            seven_letter="WILLMBG",
            fourteen_letter="WILLIAMSBURG"
        )
    )
    WINDSOR = Municipality(
        name="Windsor",
        abbreviations=PlaceAbbreviations(
            three_letter="WIN",
            five_letter="WINDS",
            seven_letter="WINDSR",
            fourteen_letter="WINDSOR"
        )
    )
    WINTER_PARK = Municipality(
        name="Winter Park",
        abbreviations=PlaceAbbreviations(
            three_letter="WPK",
            five_letter="WINTP",
            seven_letter="WINTPK",
            fourteen_letter="WINTERPARK"
        )
    )
    WOODLAND_PARK = Municipality(
        name="Woodland Park",
        abbreviations=PlaceAbbreviations(
            three_letter="WLP",
            five_letter="WDLPK",
            seven_letter="WDLNDPK",
            fourteen_letter="WOODLANDPARK"
        )
    )
    WRAY = Municipality(
        name="Wray",
        abbreviations=PlaceAbbreviations(
            three_letter="WRA",
            five_letter="WRAY",
            seven_letter="WRAY",
            fourteen_letter="WRAY"
        )
    )
    YAMPA = Municipality(
        name="Yampa",
        abbreviations=PlaceAbbreviations(
            three_letter="YMP",
            five_letter="YAMPA",
            seven_letter="YAMPA",
            fourteen_letter="YAMPA"
        )
    )
    YUMA = Municipality(
        name="Yuma",
        abbreviations=PlaceAbbreviations(
            three_letter="YUM",
            five_letter="YUMA",
            seven_letter="YUMA",
            fourteen_letter="YUMA"
        )
    )
