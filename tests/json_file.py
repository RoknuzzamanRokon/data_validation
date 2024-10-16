import json

new = ''' [
        {
            "VervotechId": 39730025,
            "ProviderHotelId": "10148648",
            "ProviderName": "Agoda",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 41448864,
            "ProviderHotelId": "6916326",
            "ProviderName": "Agoda",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 39785534,
            "ProviderHotelId": "812255",
            "ProviderName": "Agoda",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 16295482,
            "ProviderHotelId": "3746295",
            "ProviderName": "DOTW",
            "ChannelIds": [],
            "ProviderLocationCode": "21484",
            "Type": "New"
        },
        {
            "VervotechId": 70490059,
            "ProviderHotelId": "100117052",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70480452,
            "ProviderHotelId": "100226370",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490106,
            "ProviderHotelId": "100545788",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489939,
            "ProviderHotelId": "100546042",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489971,
            "ProviderHotelId": "100659013",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70488047,
            "ProviderHotelId": "100688298",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489883,
            "ProviderHotelId": "101069401",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490081,
            "ProviderHotelId": "101223157",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490127,
            "ProviderHotelId": "101456680",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489925,
            "ProviderHotelId": "101464983",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490107,
            "ProviderHotelId": "101538790",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 61886573,
            "ProviderHotelId": "101761811",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70477325,
            "ProviderHotelId": "102073078",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489923,
            "ProviderHotelId": "102089877",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70477352,
            "ProviderHotelId": "102182739",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70478101,
            "ProviderHotelId": "102315694",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70477378,
            "ProviderHotelId": "102321036",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70479015,
            "ProviderHotelId": "102424369",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489885,
            "ProviderHotelId": "102476861",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489938,
            "ProviderHotelId": "102728247",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490060,
            "ProviderHotelId": "102850805",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490116,
            "ProviderHotelId": "102868562",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490022,
            "ProviderHotelId": "102922246",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70477279,
            "ProviderHotelId": "103080057",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489880,
            "ProviderHotelId": "103145760",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489889,
            "ProviderHotelId": "103184152",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490144,
            "ProviderHotelId": "103216480",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70477348,
            "ProviderHotelId": "103402219",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489933,
            "ProviderHotelId": "103479355",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489906,
            "ProviderHotelId": "103509178",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490115,
            "ProviderHotelId": "103619464",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490148,
            "ProviderHotelId": "103653336",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490073,
            "ProviderHotelId": "103703360",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490064,
            "ProviderHotelId": "103815401",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489992,
            "ProviderHotelId": "103818781",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489894,
            "ProviderHotelId": "103858421",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489907,
            "ProviderHotelId": "103893383",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489959,
            "ProviderHotelId": "103906537",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489997,
            "ProviderHotelId": "103909529",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490003,
            "ProviderHotelId": "103911976",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489946,
            "ProviderHotelId": "103929416",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489904,
            "ProviderHotelId": "103942856",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 39599564,
            "ProviderHotelId": "103946001",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490083,
            "ProviderHotelId": "103992102",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490039,
            "ProviderHotelId": "104005313",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490071,
            "ProviderHotelId": "104153124",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489969,
            "ProviderHotelId": "104166064",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489895,
            "ProviderHotelId": "104183181",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489914,
            "ProviderHotelId": "104198492",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489929,
            "ProviderHotelId": "104276355",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489987,
            "ProviderHotelId": "104279345",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489941,
            "ProviderHotelId": "104285743",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490042,
            "ProviderHotelId": "104312159",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490120,
            "ProviderHotelId": "104355603",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490123,
            "ProviderHotelId": "104355654",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490114,
            "ProviderHotelId": "104355699",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 38384103,
            "ProviderHotelId": "104355704",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490122,
            "ProviderHotelId": "104355777",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489903,
            "ProviderHotelId": "104355783",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490164,
            "ProviderHotelId": "104355786",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489973,
            "ProviderHotelId": "104399594",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489998,
            "ProviderHotelId": "104503744",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489937,
            "ProviderHotelId": "104802066",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490045,
            "ProviderHotelId": "104812669",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489912,
            "ProviderHotelId": "104833821",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490046,
            "ProviderHotelId": "104927618",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489981,
            "ProviderHotelId": "104994916",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489953,
            "ProviderHotelId": "104998491",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489958,
            "ProviderHotelId": "105018220",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490108,
            "ProviderHotelId": "105019326",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489999,
            "ProviderHotelId": "105039283",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489932,
            "ProviderHotelId": "105041313",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490040,
            "ProviderHotelId": "105041317",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490024,
            "ProviderHotelId": "105052460",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490005,
            "ProviderHotelId": "105056501",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489975,
            "ProviderHotelId": "105057447",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490021,
            "ProviderHotelId": "105063317",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489926,
            "ProviderHotelId": "105067778",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490041,
            "ProviderHotelId": "105067961",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489990,
            "ProviderHotelId": "105067970",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489993,
            "ProviderHotelId": "105068364",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489947,
            "ProviderHotelId": "105073284",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490074,
            "ProviderHotelId": "105082933",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490047,
            "ProviderHotelId": "105084390",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489965,
            "ProviderHotelId": "105084911",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490061,
            "ProviderHotelId": "105085645",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 38914590,
            "ProviderHotelId": "105088168",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490057,
            "ProviderHotelId": "105088361",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490134,
            "ProviderHotelId": "105092025",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490143,
            "ProviderHotelId": "105092955",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490166,
            "ProviderHotelId": "105092957",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490151,
            "ProviderHotelId": "105093358",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490145,
            "ProviderHotelId": "105094379",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489972,
            "ProviderHotelId": "105099558",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490162,
            "ProviderHotelId": "105100645",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490077,
            "ProviderHotelId": "105101195",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490155,
            "ProviderHotelId": "105102052",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490007,
            "ProviderHotelId": "105111194",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490103,
            "ProviderHotelId": "105131679",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490098,
            "ProviderHotelId": "105136860",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489922,
            "ProviderHotelId": "105140457",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490159,
            "ProviderHotelId": "105150379",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490163,
            "ProviderHotelId": "105151408",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490094,
            "ProviderHotelId": "105157012",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490146,
            "ProviderHotelId": "105164590",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489902,
            "ProviderHotelId": "105169664",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489900,
            "ProviderHotelId": "105204139",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489942,
            "ProviderHotelId": "105251328",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490026,
            "ProviderHotelId": "105253111",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489977,
            "ProviderHotelId": "105260796",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489943,
            "ProviderHotelId": "105336708",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489950,
            "ProviderHotelId": "105376930",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489978,
            "ProviderHotelId": "105415111",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490058,
            "ProviderHotelId": "105486905",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490067,
            "ProviderHotelId": "105493757",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490037,
            "ProviderHotelId": "105494196",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490051,
            "ProviderHotelId": "105498703",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489980,
            "ProviderHotelId": "105516198",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489913,
            "ProviderHotelId": "105568746",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489964,
            "ProviderHotelId": "105583148",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489956,
            "ProviderHotelId": "105593127",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489919,
            "ProviderHotelId": "105618388",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490065,
            "ProviderHotelId": "105653595",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490126,
            "ProviderHotelId": "105656378",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490082,
            "ProviderHotelId": "105664046",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489882,
            "ProviderHotelId": "105669386",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489928,
            "ProviderHotelId": "105670966",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489893,
            "ProviderHotelId": "105693031",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489970,
            "ProviderHotelId": "105706923",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490104,
            "ProviderHotelId": "105711877",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490097,
            "ProviderHotelId": "105759357",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489976,
            "ProviderHotelId": "105847785",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490158,
            "ProviderHotelId": "105938466",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 64013830,
            "ProviderHotelId": "105969311",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490072,
            "ProviderHotelId": "105995667",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490004,
            "ProviderHotelId": "106017417",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489991,
            "ProviderHotelId": "106044945",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 39668914,
            "ProviderHotelId": "106085710",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490157,
            "ProviderHotelId": "106111001",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490110,
            "ProviderHotelId": "106196178",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490111,
            "ProviderHotelId": "106200281",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490089,
            "ProviderHotelId": "106210135",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490010,
            "ProviderHotelId": "106329442",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490011,
            "ProviderHotelId": "106391714",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489915,
            "ProviderHotelId": "106426726",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490014,
            "ProviderHotelId": "106445661",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489963,
            "ProviderHotelId": "106499834",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490095,
            "ProviderHotelId": "106504716",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490054,
            "ProviderHotelId": "106544628",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489960,
            "ProviderHotelId": "106558570",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489934,
            "ProviderHotelId": "106585858",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489931,
            "ProviderHotelId": "106646782",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489985,
            "ProviderHotelId": "106709189",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490109,
            "ProviderHotelId": "106713676",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489911,
            "ProviderHotelId": "106715696",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490050,
            "ProviderHotelId": "106731391",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489968,
            "ProviderHotelId": "106852319",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489879,
            "ProviderHotelId": "106890724",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490165,
            "ProviderHotelId": "106895024",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489962,
            "ProviderHotelId": "106896364",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489888,
            "ProviderHotelId": "106898470",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489442,
            "ProviderHotelId": "106917328",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489881,
            "ProviderHotelId": "106924887",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490092,
            "ProviderHotelId": "106960241",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489884,
            "ProviderHotelId": "107038180",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489988,
            "ProviderHotelId": "107043947",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490023,
            "ProviderHotelId": "107053994",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489886,
            "ProviderHotelId": "107092534",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489948,
            "ProviderHotelId": "107113369",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490112,
            "ProviderHotelId": "107142573",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490070,
            "ProviderHotelId": "107153701",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490086,
            "ProviderHotelId": "107153702",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490035,
            "ProviderHotelId": "107153838",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490137,
            "ProviderHotelId": "107153864",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490049,
            "ProviderHotelId": "107154012",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490085,
            "ProviderHotelId": "107154457",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490136,
            "ProviderHotelId": "107154709",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490036,
            "ProviderHotelId": "107165750",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 39740742,
            "ProviderHotelId": "107174007",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490130,
            "ProviderHotelId": "107174189",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490034,
            "ProviderHotelId": "107207397",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490118,
            "ProviderHotelId": "107220500",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489951,
            "ProviderHotelId": "107238495",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489952,
            "ProviderHotelId": "107238512",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490012,
            "ProviderHotelId": "107239780",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490033,
            "ProviderHotelId": "107289095",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490069,
            "ProviderHotelId": "107310231",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490150,
            "ProviderHotelId": "107396706",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489949,
            "ProviderHotelId": "107437182",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490020,
            "ProviderHotelId": "107443380",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490044,
            "ProviderHotelId": "107480274",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489891,
            "ProviderHotelId": "107520757",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489917,
            "ProviderHotelId": "107541694",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490101,
            "ProviderHotelId": "107546909",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490096,
            "ProviderHotelId": "107585688",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490075,
            "ProviderHotelId": "107600873",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490017,
            "ProviderHotelId": "107605118",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490025,
            "ProviderHotelId": "107609716",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490087,
            "ProviderHotelId": "107841796",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490009,
            "ProviderHotelId": "107951825",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490053,
            "ProviderHotelId": "107951982",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 39207877,
            "ProviderHotelId": "107984342",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489935,
            "ProviderHotelId": "108049726",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489924,
            "ProviderHotelId": "108139339",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490016,
            "ProviderHotelId": "108195215",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490100,
            "ProviderHotelId": "108198708",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489940,
            "ProviderHotelId": "108268632",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489954,
            "ProviderHotelId": "108393467",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490028,
            "ProviderHotelId": "108418928",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490142,
            "ProviderHotelId": "108477370",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490029,
            "ProviderHotelId": "108500477",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489967,
            "ProviderHotelId": "108533635",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 41462897,
            "ProviderHotelId": "108567756",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489890,
            "ProviderHotelId": "108567786",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489927,
            "ProviderHotelId": "108595902",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489974,
            "ProviderHotelId": "108717349",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 16082838,
            "ProviderHotelId": "108760800",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490153,
            "ProviderHotelId": "108782611",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490019,
            "ProviderHotelId": "108921960",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490135,
            "ProviderHotelId": "108946783",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490154,
            "ProviderHotelId": "108947362",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490156,
            "ProviderHotelId": "108954758",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490102,
            "ProviderHotelId": "108967229",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490032,
            "ProviderHotelId": "109007899",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489966,
            "ProviderHotelId": "109014983",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490002,
            "ProviderHotelId": "109016096",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490084,
            "ProviderHotelId": "109037942",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490099,
            "ProviderHotelId": "109053846",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490149,
            "ProviderHotelId": "109058442",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490062,
            "ProviderHotelId": "109068278",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 16010167,
            "ProviderHotelId": "109114591",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489955,
            "ProviderHotelId": "109125684",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490119,
            "ProviderHotelId": "109135072",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 38907341,
            "ProviderHotelId": "109137667",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70481417,
            "ProviderHotelId": "109186614",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 16570316,
            "ProviderHotelId": "109317038",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489383,
            "ProviderHotelId": "109351323",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490160,
            "ProviderHotelId": "109359606",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490113,
            "ProviderHotelId": "109411944",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 15769859,
            "ProviderHotelId": "12073517",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490139,
            "ProviderHotelId": "1372890",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490125,
            "ProviderHotelId": "15953333",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 39701504,
            "ProviderHotelId": "23182472",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 39657289,
            "ProviderHotelId": "2335505",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489930,
            "ProviderHotelId": "38920808",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 39637453,
            "ProviderHotelId": "4514861",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 32187707,
            "ProviderHotelId": "51932644",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489899,
            "ProviderHotelId": "69824175",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 41570731,
            "ProviderHotelId": "76664975",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490031,
            "ProviderHotelId": "7711",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490078,
            "ProviderHotelId": "81503593",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490129,
            "ProviderHotelId": "8397946",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490088,
            "ProviderHotelId": "8438",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 41600859,
            "ProviderHotelId": "89310092",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489918,
            "ProviderHotelId": "89792142",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489909,
            "ProviderHotelId": "89793025",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 39740703,
            "ProviderHotelId": "90987457",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489961,
            "ProviderHotelId": "91565356",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489887,
            "ProviderHotelId": "91614215",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489944,
            "ProviderHotelId": "91920688",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490043,
            "ProviderHotelId": "91920815",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490091,
            "ProviderHotelId": "91923144",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490128,
            "ProviderHotelId": "91934624",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490131,
            "ProviderHotelId": "91935013",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489897,
            "ProviderHotelId": "91935121",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489898,
            "ProviderHotelId": "91936468",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489908,
            "ProviderHotelId": "91938465",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490140,
            "ProviderHotelId": "91941393",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490001,
            "ProviderHotelId": "91941975",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490152,
            "ProviderHotelId": "91942230",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490038,
            "ProviderHotelId": "91954294",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489957,
            "ProviderHotelId": "91956740",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490063,
            "ProviderHotelId": "91957117",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489892,
            "ProviderHotelId": "91957870",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489983,
            "ProviderHotelId": "91958483",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490008,
            "ProviderHotelId": "91959445",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490079,
            "ProviderHotelId": "91959849",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490066,
            "ProviderHotelId": "91959898",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490133,
            "ProviderHotelId": "91966347",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490124,
            "ProviderHotelId": "91967151",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490052,
            "ProviderHotelId": "91967910",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490055,
            "ProviderHotelId": "91973174",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490132,
            "ProviderHotelId": "91973202",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490076,
            "ProviderHotelId": "91974016",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490013,
            "ProviderHotelId": "91975070",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490015,
            "ProviderHotelId": "91975088",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489921,
            "ProviderHotelId": "91975142",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490068,
            "ProviderHotelId": "91975213",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490027,
            "ProviderHotelId": "91979423",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70480974,
            "ProviderHotelId": "92240170",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70485734,
            "ProviderHotelId": "92509860",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 15314428,
            "ProviderHotelId": "92745304",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70477318,
            "ProviderHotelId": "92938436",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490018,
            "ProviderHotelId": "93596626",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 43531385,
            "ProviderHotelId": "94911525",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489901,
            "ProviderHotelId": "94978660",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490161,
            "ProviderHotelId": "95418952",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489910,
            "ProviderHotelId": "95681533",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 41568649,
            "ProviderHotelId": "95685424",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490138,
            "ProviderHotelId": "95738215",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489982,
            "ProviderHotelId": "95769212",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489896,
            "ProviderHotelId": "95968206",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490030,
            "ProviderHotelId": "96763900",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489905,
            "ProviderHotelId": "96832125",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489936,
            "ProviderHotelId": "96845693",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70477365,
            "ProviderHotelId": "96972507",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490105,
            "ProviderHotelId": "97051702",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489995,
            "ProviderHotelId": "99339824",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489986,
            "ProviderHotelId": "99339864",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70490117,
            "ProviderHotelId": "99543093",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70478849,
            "ProviderHotelId": "99543938",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70485277,
            "ProviderHotelId": "99544874",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70489916,
            "ProviderHotelId": "99670513",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 70477343,
            "ProviderHotelId": "99991963",
            "ProviderName": "EAN",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 15558651,
            "ProviderHotelId": "JP065239",
            "ProviderName": "EscalaBeds",
            "ChannelIds": [],
            "ProviderLocationCode": "2168",
            "Type": "New"
        },
        {
            "VervotechId": 15301294,
            "ProviderHotelId": "1544140",
            "ProviderName": "GRNConnect",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 38923472,
            "ProviderHotelId": "1592895",
            "ProviderName": "GRNConnect",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 15558651,
            "ProviderHotelId": "156180",
            "ProviderName": "GoGlobal",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 38923472,
            "ProviderHotelId": "70347",
            "ProviderName": "GoGlobal",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 39642196,
            "ProviderHotelId": "47189",
            "ProviderName": "HyperGuestDirect",
            "ChannelIds": [],
            "ProviderLocationCode": null,
            "Type": "New"
        },
        {
            "VervotechId": 15383133,
            "ProviderHotelId": "AS10000002",
            "ProviderName": "MGHoliday",
            "ChannelIds": [
                "NonDirectContract"
            ],
            "ProviderLocationCode": "AS-PPG",
            "Type": "New"
        },
        {
            "VervotechId": 38739888,
            "ProviderHotelId": "PF10000054",
            "ProviderName": "MGHoliday",
            "ChannelIds": [
                "NonDirectContract"
            ],
            "ProviderLocationCode": "PF-THI",
            "Type": "New"
        },
        {
            "VervotechId": 15558651,
            "ProviderHotelId": "ZkSV",
            "ProviderName": "Rakuten",
            "ChannelIds": [],
            "ProviderLocationCode": "",
            "Type": "New"
        },
        {
            "VervotechId": 17435281,
            "ProviderHotelId": "1559016",
            "ProviderName": "TBO",
            "ChannelIds": [
                "TBOHotels",
                "TopHotels"
            ],
            "ProviderLocationCode": "122471",
            "Type": "New"
        },
        {
            "VervotechId": 16378343,
            "ProviderHotelId": "1738666",
            "ProviderName": "TBO",
            "ChannelIds": [
                "TBOHotels",
                "TopHotels"
            ],
            "ProviderLocationCode": "122352",
            "Type": "New"
        },
        {
            "VervotechId": 70490080,
            "ProviderHotelId": "5587962",
            "ProviderName": "TBO",
            "ChannelIds": [
                "TopHotels"
            ],
            "ProviderLocationCode": "100636",
            "Type": "New"
        },
        {
            "VervotechId": 70483528,
            "ProviderHotelId": "6272152",
            "ProviderName": "TBO",
            "ChannelIds": [
                "TBOHotels"
            ],
            "ProviderLocationCode": "123347",
            "Type": "New"
        },
        {
            "VervotechId": 70482995,
            "ProviderHotelId": "6273461",
            "ProviderName": "TBO",
            "ChannelIds": [
                "TBOHotels"
            ],
            "ProviderLocationCode": "123347",
            "Type": "New"
        }
    ]'''


data = json.dumps(new)

print(data)
print(len(data))