import requests

cookies = {
    '__vst': 'b8c4d6b9-62f3-4108-b45f-0dbe2d59f293',
    '__ssn': 'cc74e43c-6e1a-47c0-aae5-ba40fdb92788',
    '__ssnstarttime': '1689882148',
    'split': 'n',
    'split_tcv': '183',
    '__bot': 'false',
    'AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg': '1',
    's_ecid': 'MCMID%7C73995613563923143472010543520208612815',
    'permutive-id': 'f72411d4-49a7-4045-a82f-60ee34950fb9',
    'AMCV_8853394255142B6A0A4C98A4%40AdobeOrg': '-1124106680%7CMCIDTS%7C19559%7CMCMID%7C73995613563923143472010543520208612815%7CMCAAMLH-1690486951%7C3%7CMCAAMB-1690486951%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1689889352s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19566%7CvVersion%7C5.2.0',
    '_tac': 'false~self|not-available',
    '_ta': 'us~1~89df68bc35032d48c293adce8574aa42',
    '_tas': 'vqcr1eyto8m',
    '_gcl_au': '1.1.1416639863.1689882159',
    'pxcts': '95590366-2735-11ee-a5e0-787658436651',
    '_pxvid': '9558f27a-2735-11ee-a5e0-0eaa2a7b87ac',
    '_tt_enable_cookie': '1',
    '_ttp': 't4VGEzUYfC3rB8gCFiJZuGxHCyn',
    'AMCVS_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg': '1',
    'AMCV_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg': '-1124106680%7CMCMID%7C73995613563923143472010543520208612815%7CMCIDTS%7C19559%7CMCOPTOUT-1689889360s%7CNONE%7CvVersion%7C5.2.0',
    'ajs_anonymous_id': 'c140c574-cbb6-4155-aecb-3e2b6f070293',
    '_gid': 'GA1.2.1643516151.1689882163',
    'AWSALBTG': 'Y55rjL1dhkX78BjIsqA+XGoATVpsvqlz33rrkD9/eTj7Yj7wxOd+l0hVwOIZoNSbzwsA+zVR/CnC27tHePzMCQtmvcnsPeb9NdBGXBrNtopJLva6OQWTQST70AMkUjy6/Q98lVmZubD+3Gd25NT3nuU3I0O17mhrGbUYfMZy58QSziRp+09VkA7wYJnB85hW9M6r1tHbXHCKyHCimmcbjDHH+q+yHVC6eNLvGq/YbVNSfCzWljb1XYshJoyQYzYo',
    'AWSALBTGCORS': 'Y55rjL1dhkX78BjIsqA+XGoATVpsvqlz33rrkD9/eTj7Yj7wxOd+l0hVwOIZoNSbzwsA+zVR/CnC27tHePzMCQtmvcnsPeb9NdBGXBrNtopJLva6OQWTQST70AMkUjy6/Q98lVmZubD+3Gd25NT3nuU3I0O17mhrGbUYfMZy58QSziRp+09VkA7wYJnB85hW9M6r1tHbXHCKyHCimmcbjDHH+q+yHVC6eNLvGq/YbVNSfCzWljb1XYshJoyQYzYo',
    'AWSALB': 'uBo8sKDi5n3koBCiTQEy99yt7KjrDuDcDcipGq9jQd7867ReEgjxBsvlKbCg98uns0Kwf153RziXragTWwGYieBocP8U+G16t9S3pP9Jp8b5tqv4UYlSJfZ2JOr1',
    'AWSALBCORS': 'uBo8sKDi5n3koBCiTQEy99yt7KjrDuDcDcipGq9jQd7867ReEgjxBsvlKbCg98uns0Kwf153RziXragTWwGYieBocP8U+G16t9S3pP9Jp8b5tqv4UYlSJfZ2JOr1',
    'G_ENABLED_IDPS': 'google',
    'cebs': '1',
    '_ce.clock_event': '1',
    'cebsp_': '1',
    '_ce.s': 'v~0e1cab85d6d828700593376a122cd06134a78987~lcw~1689882188848~vpv~0~v11.rlc~1689882190386~lcw~1689882190387',
    '_ce.clock_data': '309%2C39.41.171.169%2C1%2Ce67aa3dbeb858df8c9104ff079c477f2',
    'mdLogger': 'false',
    'kampyle_userid': '0d26-69c7-0cbf-143d-0afd-dbe3-fc2a-431d',
    'kampyleUserSession': '1689882197498',
    'kampyleUserSessionsCount': '1',
    '_ga_VFQNX1P1DT': 'GS1.1.1689882198.1.1.1689882214.44.0.0',
    'g_state': '{"i_p":1689889587940,"i_l":1}',
    '_pbjs_userid_consent_data': '3524755945110770',
    'adcloud': '{%22_les_v%22:%22y%2Crealtor.com%2C1689884193%22}',
    '_ncg_sp_ses.cc72': '*',
    '_ncg_id_': 'a6884cc7-4e16-4d6b-9118-bb21e0e58558',
    '__split': '80',
    '_ncg_domain_id_': 'a6884cc7-4e16-4d6b-9118-bb21e0e58558.1.1689882397160.1752954397160',
    '_ncg_sp_id.cc72': 'a6884cc7-4e16-4d6b-9118-bb21e0e58558.1689882397.1.1689882400.1689882397.09b3b0d6-7600-4134-874d-7bb5f85e53e5',
    'ab.storage.userId.7cc9d032-9d6d-44cf-a8f5-d276489af322': '%7B%22g%22%3A%22visitor_b8c4d6b9-62f3-4108-b45f-0dbe2d59f293%22%2C%22c%22%3A1689882401343%2C%22l%22%3A1689882401353%7D',
    'ab.storage.deviceId.7cc9d032-9d6d-44cf-a8f5-d276489af322': '%7B%22g%22%3A%22f8b1f8f3-734e-2e58-d50d-e2bdd29b3ae9%22%2C%22c%22%3A1689882401359%2C%22l%22%3A1689882401359%7D',
    'ab.storage.sessionId.7cc9d032-9d6d-44cf-a8f5-d276489af322': '%7B%22g%22%3A%22f1372721-ab4d-952c-7b43-78425e49c71c%22%2C%22e%22%3A1689884201373%2C%22c%22%3A1689882401349%2C%22l%22%3A1689882401373%7D',
    '__gsas': 'ID=6da571504b499b62:T=1689882397:RT=1689882397:S=ALNI_MZKitpfC9iFdMqZpPot-7ioD3o1Nw',
    '_ncg_g_id_': '2f130543-4ad3-4df3-b7b6-4e74b9fe6985.3.1689882400.1752954397160',
    '__qca': 'P0-954955490-1689882397117',
    '_ga': 'GA1.2.802351445.1689882161',
    '_uetsid': '97863a70273511ee8c6743903ee3802c',
    '_uetvid': '97869150273511ee95a4a3567aee71c9',
    'kampyleSessionPageCounter': '2',
    'kampyleUserPercentile': '2.247716457557769',
    'QSI_HistorySession': 'https%3A%2F%2Fwww.realtor.com%2Frealestateagency%2Faustin_tx%2Fpg-70~1689882166842%7Chttps%3A%2F%2Fwww.realtor.com%2Fterms-of-service%2F~1689882198147%7Chttps%3A%2F%2Fwww.realtor.com%2Fsitemap~1689882198959%7Chttps%3A%2F%2Fwww.realtor.com%2Fprivacy-policy%2F~1689882199052%7Chttps%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-search%2FNew-York_NY~1689882412987',
    'QSI_SI_cN5gYlOK8LtV3pz_intercept': 'true',
    '_px3': '575cac93ba9314d6bd8d4ba26b480e2b9e8b5db07055653afe0fab83b991e934:wZlgCZ1t5g2ojqnSVM4z8V2PAHNUHmvBGQlhRyOvgmMxVM3Gzly9P786UipIw30xnHQLbX7BCGG6/4p8Neelow==:1000:cohMUeBuxMMUUfGyo28sMWT0Dzc6xz58raZNVjHLvXi5RzI9ePRnxlIIsrDGxeEqB4qh/p/H7x5h86OAgajdlqbwXpWV4qI/giQKSIlECQCpiw+xV8B8bMBH65+M41dDb24D3cW8OaWyr9gBuGIMrZGgHFCYx5bcKU7ZO7g1AJDjDe8CEBpMtsnrpiYYksyK9cNJDaNPeeUW83c2UegjoA==',
    '_ga_MS5EHT6J6V': 'GS1.1.1689882160.1.1.1689882718.0.0.0',
}

headers = {
    'authority': 'www.realtor.com',
    'accept': 'application/json, text/javascript',
    'accept-language': 'en-GB,en;q=0.9,ur-PK;q=0.8,ur;q=0.7,en-US;q=0.6',
    'content-type': 'application/json',
    # 'cookie': '__vst=b8c4d6b9-62f3-4108-b45f-0dbe2d59f293; __ssn=cc74e43c-6e1a-47c0-aae5-ba40fdb92788; __ssnstarttime=1689882148; split=n; split_tcv=183; __bot=false; AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg=1; s_ecid=MCMID%7C73995613563923143472010543520208612815; permutive-id=f72411d4-49a7-4045-a82f-60ee34950fb9; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCIDTS%7C19559%7CMCMID%7C73995613563923143472010543520208612815%7CMCAAMLH-1690486951%7C3%7CMCAAMB-1690486951%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1689889352s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19566%7CvVersion%7C5.2.0; _tac=false~self|not-available; _ta=us~1~89df68bc35032d48c293adce8574aa42; _tas=vqcr1eyto8m; _gcl_au=1.1.1416639863.1689882159; pxcts=95590366-2735-11ee-a5e0-787658436651; _pxvid=9558f27a-2735-11ee-a5e0-0eaa2a7b87ac; _tt_enable_cookie=1; _ttp=t4VGEzUYfC3rB8gCFiJZuGxHCyn; AMCVS_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=1; AMCV_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCMID%7C73995613563923143472010543520208612815%7CMCIDTS%7C19559%7CMCOPTOUT-1689889360s%7CNONE%7CvVersion%7C5.2.0; ajs_anonymous_id=c140c574-cbb6-4155-aecb-3e2b6f070293; _gid=GA1.2.1643516151.1689882163; AWSALBTG=Y55rjL1dhkX78BjIsqA+XGoATVpsvqlz33rrkD9/eTj7Yj7wxOd+l0hVwOIZoNSbzwsA+zVR/CnC27tHePzMCQtmvcnsPeb9NdBGXBrNtopJLva6OQWTQST70AMkUjy6/Q98lVmZubD+3Gd25NT3nuU3I0O17mhrGbUYfMZy58QSziRp+09VkA7wYJnB85hW9M6r1tHbXHCKyHCimmcbjDHH+q+yHVC6eNLvGq/YbVNSfCzWljb1XYshJoyQYzYo; AWSALBTGCORS=Y55rjL1dhkX78BjIsqA+XGoATVpsvqlz33rrkD9/eTj7Yj7wxOd+l0hVwOIZoNSbzwsA+zVR/CnC27tHePzMCQtmvcnsPeb9NdBGXBrNtopJLva6OQWTQST70AMkUjy6/Q98lVmZubD+3Gd25NT3nuU3I0O17mhrGbUYfMZy58QSziRp+09VkA7wYJnB85hW9M6r1tHbXHCKyHCimmcbjDHH+q+yHVC6eNLvGq/YbVNSfCzWljb1XYshJoyQYzYo; AWSALB=uBo8sKDi5n3koBCiTQEy99yt7KjrDuDcDcipGq9jQd7867ReEgjxBsvlKbCg98uns0Kwf153RziXragTWwGYieBocP8U+G16t9S3pP9Jp8b5tqv4UYlSJfZ2JOr1; AWSALBCORS=uBo8sKDi5n3koBCiTQEy99yt7KjrDuDcDcipGq9jQd7867ReEgjxBsvlKbCg98uns0Kwf153RziXragTWwGYieBocP8U+G16t9S3pP9Jp8b5tqv4UYlSJfZ2JOr1; G_ENABLED_IDPS=google; cebs=1; _ce.clock_event=1; cebsp_=1; _ce.s=v~0e1cab85d6d828700593376a122cd06134a78987~lcw~1689882188848~vpv~0~v11.rlc~1689882190386~lcw~1689882190387; _ce.clock_data=309%2C39.41.171.169%2C1%2Ce67aa3dbeb858df8c9104ff079c477f2; mdLogger=false; kampyle_userid=0d26-69c7-0cbf-143d-0afd-dbe3-fc2a-431d; kampyleUserSession=1689882197498; kampyleUserSessionsCount=1; _ga_VFQNX1P1DT=GS1.1.1689882198.1.1.1689882214.44.0.0; g_state={"i_p":1689889587940,"i_l":1}; _pbjs_userid_consent_data=3524755945110770; adcloud={%22_les_v%22:%22y%2Crealtor.com%2C1689884193%22}; _ncg_sp_ses.cc72=*; _ncg_id_=a6884cc7-4e16-4d6b-9118-bb21e0e58558; __split=80; _ncg_domain_id_=a6884cc7-4e16-4d6b-9118-bb21e0e58558.1.1689882397160.1752954397160; _ncg_sp_id.cc72=a6884cc7-4e16-4d6b-9118-bb21e0e58558.1689882397.1.1689882400.1689882397.09b3b0d6-7600-4134-874d-7bb5f85e53e5; ab.storage.userId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%22visitor_b8c4d6b9-62f3-4108-b45f-0dbe2d59f293%22%2C%22c%22%3A1689882401343%2C%22l%22%3A1689882401353%7D; ab.storage.deviceId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%22f8b1f8f3-734e-2e58-d50d-e2bdd29b3ae9%22%2C%22c%22%3A1689882401359%2C%22l%22%3A1689882401359%7D; ab.storage.sessionId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%22f1372721-ab4d-952c-7b43-78425e49c71c%22%2C%22e%22%3A1689884201373%2C%22c%22%3A1689882401349%2C%22l%22%3A1689882401373%7D; __gsas=ID=6da571504b499b62:T=1689882397:RT=1689882397:S=ALNI_MZKitpfC9iFdMqZpPot-7ioD3o1Nw; _ncg_g_id_=2f130543-4ad3-4df3-b7b6-4e74b9fe6985.3.1689882400.1752954397160; __qca=P0-954955490-1689882397117; _ga=GA1.2.802351445.1689882161; _uetsid=97863a70273511ee8c6743903ee3802c; _uetvid=97869150273511ee95a4a3567aee71c9; kampyleSessionPageCounter=2; kampyleUserPercentile=2.247716457557769; QSI_HistorySession=https%3A%2F%2Fwww.realtor.com%2Frealestateagency%2Faustin_tx%2Fpg-70~1689882166842%7Chttps%3A%2F%2Fwww.realtor.com%2Fterms-of-service%2F~1689882198147%7Chttps%3A%2F%2Fwww.realtor.com%2Fsitemap~1689882198959%7Chttps%3A%2F%2Fwww.realtor.com%2Fprivacy-policy%2F~1689882199052%7Chttps%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-search%2FNew-York_NY~1689882412987; QSI_SI_cN5gYlOK8LtV3pz_intercept=true; _px3=575cac93ba9314d6bd8d4ba26b480e2b9e8b5db07055653afe0fab83b991e934:wZlgCZ1t5g2ojqnSVM4z8V2PAHNUHmvBGQlhRyOvgmMxVM3Gzly9P786UipIw30xnHQLbX7BCGG6/4p8Neelow==:1000:cohMUeBuxMMUUfGyo28sMWT0Dzc6xz58raZNVjHLvXi5RzI9ePRnxlIIsrDGxeEqB4qh/p/H7x5h86OAgajdlqbwXpWV4qI/giQKSIlECQCpiw+xV8B8bMBH65+M41dDb24D3cW8OaWyr9gBuGIMrZGgHFCYx5bcKU7ZO7g1AJDjDe8CEBpMtsnrpiYYksyK9cNJDaNPeeUW83c2UegjoA==; _ga_MS5EHT6J6V=GS1.1.1689882160.1.1.1689882718.0.0.0',
    'dnt': '1',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM3ODU4NCIsImFwIjoiOTAwMDM5MzQ1IiwiaWQiOiJiZGQ2Y2YzNTY3MzU3N2UwIiwidHIiOiI3NmUzNTVjNGYxNjkzOGJlMzg2NjFkZmU3ZmMzMjUwMCIsInRpIjoxNjg5ODgyNzIwOTczLCJ0ayI6IjEwMjI2ODEifX0=',
    'origin': 'https://www.realtor.com',
    'referer': 'https://www.realtor.com/realestateandhomes-search/New-York_NY',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-76e355c4f16938be38661dfe7fc32500-bdd6cf35673577e0-01',
    'tracestate': '1022681@nr=0-1-378584-900039345-bdd6cf35673577e0----1689882720973',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

params = {
    'client_id': 'rdc-search-for-sale-search',
    'schema': 'vesta',
}

json_data = {
    'query': '\n  query ConsumerSearchQuery(\n    $query: HomeSearchCriteria!\n    $limit: Int\n    $offset: Int\n    $search_promotion: SearchPromotionInput\n    $sort: [SearchAPISort]\n    $sort_type: SearchSortType\n    $client_data: JSON\n    $bucket: SearchAPIBucket\n  ) {\n    home_search: home_search(\n      query: $query\n      sort: $sort\n      limit: $limit\n      offset: $offset\n      sort_type: $sort_type\n      client_data: $client_data\n      bucket: $bucket\n      search_promotion: $search_promotion\n    ) {\n      count\n      total\n      search_promotion {\n        name\n        slots\n        promoted_properties {\n          id\n          from_other_page\n        }\n      }\n      properties: results {\n        property_id\n        list_price\n        search_promotions {\n          name\n          asset_id\n        }\n        primary_photo(https: true) {\n          href\n        }\n        rent_to_own {\n          right_to_purchase\n          rent\n        }\n        listing_id\n        matterport\n        virtual_tours {\n          href\n          type\n        }\n        status\n        products {\n          products\n        }\n        source {\n          id\n          type\n          spec_id\n          plan_id\n          agents {\n            office_name\n          }\n        }\n        lead_attributes {\n          show_contact_an_agent\n          opcity_lead_attributes {\n            cashback_enabled\n            flip_the_market_enabled\n          }\n          lead_type\n          ready_connect_mortgage {\n            show_contact_a_lender\n            show_veterans_united\n          }\n        }\n        community {\n          description {\n            name\n          }\n          property_id\n          permalink\n          advertisers {\n            office {\n              hours\n              phones {\n                type\n                number\n                primary\n                trackable\n              }\n            }\n          }\n          promotions {\n            description\n            href\n            headline\n          }\n        }\n        permalink\n        price_reduced_amount\n        description {\n          name\n          beds\n          baths_consolidated\n          sqft\n          lot_sqft\n          baths_max\n          baths_min\n          beds_min\n          beds_max\n          sqft_min\n          sqft_max\n          type\n          sub_type\n          sold_price\n          sold_date\n        }\n        location {\n          address {\n            line\n            postal_code\n            state\n            state_code\n            city\n            coordinate {\n              lat\n              lon\n            }\n          }\n          county {\n            name\n            fips_code\n          }\n        }\n        open_houses {\n          start_date\n          end_date\n        }\n        branding {\n          type\n          name\n          photo\n        }\n        flags {\n          is_coming_soon\n          is_new_listing(days: 14)\n          is_price_reduced(days: 30)\n          is_foreclosure\n          is_new_construction\n          is_pending\n          is_contingent\n        }\n        list_date\n        photos(limit: 2, https: true) {\n          href\n        }\n      }\n    }\n  }\n',
    'variables': {
        'geoSupportedSlug': 'New-York_NY',
        'query': {
            'primary': True,
            'status': [
                'for_sale',
                'ready_to_build',
            ],
            'search_location': {
                'location': 'New York, NY',
            },
        },
        'client_data': {
            'device_data': {
                'device_type': 'desktop',
            },
        },
        'limit': 42,
        'offset': 42,
        'sort_type': 'relevant',
        'bucket': {
            'sort': 'fractal_v1.1.3',
        },
        'search_promotion': {
            'name': 'CITY',
            'slots': [],
            'promoted_properties': [
                [],
            ],
        },
    },
    'seoPayload': {
        'asPath': '/realestateandhomes-search/New-York_NY/pg-2',
        'pageType': {
            'silo': 'search_result_page',
            'status': 'for_sale',
        },
        'county_needed_for_uniq': False,
        'isFaqSupport': True,
    },
    'visitor_id': 'b8c4d6b9-62f3-4108-b45f-0dbe2d59f293',
}

response = requests.post(
    'https://www.realtor.com/api/v1/rdc_search_srp',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)


response.json()