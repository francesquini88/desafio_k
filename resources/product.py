from flask_restful import Resource, reqparse
from models.product import ProductModel

products = [
  {
    "brinde": "",
    "oferta": {
      "codigo": "859Hj0ZF8.RNg",
      "evento_codigo": 108,
      "data_inicio": 1593808200,
      "data_fim": 1596225600,
      "quantidade": 906,
      "evento": "Julho Gamer",
      "logar": 0
    },
    "oferta_inicio": 0,
    "nova_descricao": "index.html",
    "menus": [
      {
        "codigo": 1,
        "nome": "Hardware",
        "amigavel": "/hardware",
        "nome_url": "/Hardware"
      },
      {
        "codigo": 105,
        "nome": "SATA",
        "amigavel": "/hardware/ssd-2-5",
        "nome_url": "/Hardware/SATA"
      },
      {
        "codigo": 1231,
        "nome": "240.0 GB",
        "amigavel": "/hardware/ssd-2-5/240-0-gb",
        "nome_url": "/Hardware/SATA/240.0 GB"
      },
      {
        "codigo": 1432,
        "nome": "SSD",
        "amigavel": "/hardware/ssd-2-5/240-0-gb/ssd-2-5",
        "nome_url": "/Hardware/SATA/240.0 GB/SSD"
      }
    ],
    "menu": "Hardware/SATA/240.0 GB/SSD",
    "codigo": 85197,
    "nome": "SSD Kingston A400, 240GB, SATA, Leitura 500MB/s, Grava\u00e7\u00e3o 350MB/s - SA400S37/240G",
    "familia": {
      "codigo": 0,
      "nome": "Kingston",
      "titulo": "Fabricante",
      "produtos": [
        {
          "codigo": 85198,
          "nome": "SSD Kingston A400, 480GB, SATA, Leitura 500MB/s, Grava\u00e7\u00e3o 450MB/s - SA400S37/480G",
          "preco": 588.12,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 499.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/85198/ssd-kingston-a400-480gb-sata-leitura-500mb-s-grava-o-450mb-s-sa400s37-480g",
          "foto": "https://images8.kabum.com.br/produtos/fotos/85198/85198_index_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 85196,
          "nome": "SSD Kingston A400, 120GB, SATA, Leitura 500MB/s, Grava\u00e7\u00e3o 320MB/s - SA400S37/120G",
          "preco": 235.18,
          "preco_prime": 0.0,
          "preco_antigo": 317.53,
          "disponibilidade": "",
          "preco_desconto": 199.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/85196/ssd-kingston-a400-120gb-sata-leitura-500mb-s-grava-o-320mb-s-sa400s37-120g",
          "foto": "https://images6.kabum.com.br/produtos/fotos/85196/85196_index_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 95217,
          "nome": "SSD Kingston A400, 960GB, SATA, Leitura 500MB/s, Grava\u00e7\u00e3o 450MB/s - SA400S37/960G",
          "preco": 941.06,
          "preco_prime": 1294.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 799.9,
          "preco_desconto_prime": 1099.9,
          "link_descricao": "/produto/95217/ssd-kingston-a400-960gb-sata-leitura-500mb-s-grava-o-450mb-s-sa400s37-960g",
          "foto": "https://images7.kabum.com.br/produtos/fotos/95217/95217_1520016948_index_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 107339,
          "nome": "SSD Kingston KC600, 512GB, SATA, Leitura 550MB/s, Grava\u00e7\u00e3o 520MB/s - SKC600/512G",
          "preco": 670.47,
          "preco_prime": 0.0,
          "preco_antigo": 779.88,
          "disponibilidade": "",
          "preco_desconto": 569.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/107339/ssd-kingston-kc600-512gb-sata-leitura-550mb-s-grava-o-520mb-s-skc600-512g",
          "foto": "https://images9.kabum.com.br/produtos/fotos/107339/ssd-kingston-kc600-512gb-sata-leitura-550mb-s-gravacao-520mb-s-skc600-512g_1572360201_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 107338,
          "nome": "SSD Kingston KC600, 256GB, SATA, Leitura 550MB/s, Grava\u00e7\u00e3o 500MB/s - SKC600/256G",
          "preco": 435.18,
          "preco_prime": 0.0,
          "preco_antigo": 482.24,
          "disponibilidade": "",
          "preco_desconto": 369.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/107338/ssd-kingston-kc600-256gb-sata-leitura-550mb-s-grava-o-500mb-s-skc600-256g",
          "foto": "https://images8.kabum.com.br/produtos/fotos/107338/ssd-kingston-kc600-256gb-sata-leitura-550mb-s-gravacao-500mb-s-skc600-256g_1572354349_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 108159,
          "nome": "SSD Kingston A400, 1920GB, SATA, Leitura 500MB/s, Grava\u00e7\u00e3o 450MB/s - SA400S37/1920G",
          "preco": 1898.71,
          "preco_prime": 0.0,
          "preco_antigo": 2177.53,
          "disponibilidade": "",
          "preco_desconto": 1613.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/108159/ssd-kingston-a400-1920gb-sata-leitura-500mb-s-grava-o-450mb-s-sa400s37-1920g",
          "foto": "https://images9.kabum.com.br/produtos/fotos/108159/ssd-kingston-a400-1920gb-sata-leitura-500mb-s-gravacao-450mb-s-sa400s37-1920g_1579023050_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 107340,
          "nome": "SSD Kingston KC600, 1024GB, SATA, Leitura 550MB/s, Grava\u00e7\u00e3o 520MB/s - SKC600/1024G",
          "preco": 1305.76,
          "preco_prime": 0.0,
          "preco_antigo": 1419.88,
          "disponibilidade": "",
          "preco_desconto": 1109.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/107340/ssd-kingston-kc600-1024gb-sata-leitura-550mb-s-grava-o-520mb-s-skc600-1024g",
          "foto": "https://images0.kabum.com.br/produtos/fotos/107340/ssd-kingston-kc600-1024gb-sata-leitura-550mb-s-gravacao-520mb-s-skc600-1024g_ssd-kingston-kc600-1024gb-sata-leitura-550mb-s-gravacao-520mb-s-skc600-1024g_1572361632_m.jpg",
          "produto_prime": ""
        }
      ]
    },
    "fotos": [
      "https://images7.kabum.com.br/produtos/fotos/85197/85197_index_g.jpg",
      "https://images7.kabum.com.br/produtos/fotos/85197/85197_1484306076_g.jpg",
      "https://images7.kabum.com.br/produtos/fotos/85197/85197_1484306080_g.jpg"
    ],
    "disponibilidade": "",
    "pre_venda": "",
    "fabricante": {
      "codigo": 50,
      "nome": "Kingston",
      "img": "https://images0.kabum.com.br/produtos/fabricantes/logo-kingston.jpg"
    },
    "preco": 329.29,
    "preco_prime": 0.0,
    "preco_desconto": 279.9,
    "preco_desconto_prime": 0.0,
    "preco_antigo": 446.94,
    "economize_prime": 279.9,
    "descricao": "Conhe\u00e7a o SSD A400 da Kingston. Performance incr\u00edvel e tecnologia de ponta! Este SSD possui com a tecnologia 3D NAND (tamb\u00e9m chamada de V-NAND). \n\nPerformance n\u00e3o ser\u00e1 problema com este SSD. Ele possui uma controladora de \u00faltima gera\u00e7\u00e3o para velocidades de leitura e grava\u00e7\u00e3o de at\u00e9 500MB/s e 350MB/s, este SSD \u00e9 10x mais r\u00e1pido do que um HD tradicional para melhor desempenho, resposta ultrarr\u00e1pida em multitarefas e um computador mais r\u00e1pido de modo geral. O seu desktop merece esse grande upgrade de velocidade!\n\nComparados a discos r\u00edgidos mec\u00e2nicos, o SSD A400 aumenta de forma dr\u00e1stica a resposta do seu PC com tempos maravilhosos de inicializa\u00e7\u00e3o, carregamento e transfer\u00eancia. \n\nAl\u00e9m dessa performance incr\u00edvel, este SSD tamb\u00e9m \u00e9 mais confi\u00e1vel e dur\u00e1vel do que um disco r\u00edgido comum. Este A400 possui 240GB de capacidade, o tamanho certo para o que voc\u00ea precisa no dia a dia. Procurando SSD? Compre no KaBuM!",
    "tag_title": "",
    "tem_frete_gratis": "",
    "frete_gratis_somente_prime": "",
    "tag_description": "",
    "avaliacao_numero": 2141,
    "avaliacao_nota": 5,
    "desconto": 15,
    "is_openbox": "",
    "produto_html": "<p><strong>Caracter&iacute;sticas:</strong></p><p>- Marca: Kingston</p><p>- Modelo: SA400S37/240G</p><p>&nbsp;</p><p><strong>Especifica&ccedil;&otilde;es:</strong></p><p>- Formato: 2,5 pol&nbsp;</p><p>- Interface: SATA Rev. 3.0 (6Gb/s) &mdash; compat&iacute;vel com a vers&atilde;o anterior SATA Rev. 2.0 (3Gb/s)</p><p>- Capacidades: 240GB</p><p>- NAND: TLC&nbsp;</p><p>- Performance de refer&ecirc;ncia - at&eacute; 500MB/s para leitura e 350MB/s para grava&ccedil;&atilde;o&nbsp;</p><p>- Temperatura de armazenamento: -40 &deg;C a 85 &deg;C&nbsp;</p><p>- Temperatura de opera&ccedil;&atilde;o: 0 &deg;C a 70 &deg;C</p><p>- Vibra&ccedil;&atilde;o quando em opera&ccedil;&atilde;o: 2,17G pico (7 &ndash; 800 Hz)</p><p>- Vibra&ccedil;&atilde;o quando n&atilde;o est&aacute; em opera&ccedil;&atilde;o: 20G pico (10 &ndash; 2000 Hz)</p><p>- Expectativa de vida &uacute;til: 1 milh&atilde;o de horas MTB</p><p>&nbsp;</p><p><strong>Benef&iacute;cios:&nbsp;</strong></p><p>- 10x mais r&aacute;pido do que um disco r&iacute;gido: Com incr&iacute;veis velocidades de leitura/grava&ccedil;&atilde;o, o SSD A400 n&atilde;o somente ir&aacute; aumentar o desempenho, como tamb&eacute;m poder&aacute; ser usado para dar vida nova em computadores mais antigos.&nbsp;</p><p>- Robusto: O A400 &eacute; resistente a impactos e vibra&ccedil;&otilde;es, para confiabilidade refor&ccedil;ada em notebooks e outros dispositivos m&oacute;veis.&nbsp;</p><p>- Ideal para desktops e notebooks: A400 tem um formato de 7 mm parase ajustar auma grande variedade de computadores. &Eacute; ideal para notebooks mais finos e computadores, ultrabooks e ultratop com espa&ccedil;o limitado.</p><p><strong><br /></strong></p><p><strong>Conte&uacute;do da embalagem:</strong></p><p>- SSD Kingston</p>",
    "dimensao_peso": 70,
    "peso": "70 gramas (bruto com embalagem)",
    "garantia": "1 ano de garantia",
    "codigo_anatel": "",
    "produto_especie": 0,
    "link_descricao": "/produto/85197/ssd-kingston-a400-240gb-sata-leitura-500mb-s-grava-o-350mb-s-sa400s37-240g",
    "origem": "",
    "origem_nome": "",
    "flag_blackfriday": 0,
    "sucesso": ""
  },
  {
    "brinde": "",
    "oferta": "",
    "oferta_inicio": 0,
    "menus": [
      {
        "codigo": 1,
        "nome": "Hardware",
        "amigavel": "/hardware",
        "nome_url": "/Hardware"
      },
      {
        "codigo": 11,
        "nome": "Mem\u00f3ria RAM",
        "amigavel": "/hardware/memoria-ram",
        "nome_url": "/Hardware/Mem\u00f3ria RAM"
      },
      {
        "codigo": 6558,
        "nome": "DDR 4",
        "amigavel": "/hardware/memoria-ram/ddr-4",
        "nome_url": "/Hardware/Mem\u00f3ria RAM/DDR 4"
      },
      {
        "codigo": 6702,
        "nome": "2400MHz",
        "amigavel": "/hardware/memoria-ram/ddr-4/2400mhz",
        "nome_url": "/Hardware/Mem\u00f3ria RAM/DDR 4/2400MHz"
      }
    ],
    "menu": "Hardware/Mem\u00f3ria RAM/DDR 4/2400MHz",
    "codigo": 79936,
    "nome": "Mem\u00f3ria HyperX Fury, 8GB, 2400MHz, DDR4, CL15, Preto - HX424C15FB2/8",
    "familia": {
      "codigo": 0,
      "nome": "Hyperx",
      "titulo": "Fabricante",
      "produtos": [
        {
          "codigo": 103946,
          "nome": "Mem\u00f3ria HyperX Fury, 8GB, 2400MHz, DDR4, CL15, Preto - HX424C15FB3/8",
          "preco": 364.59,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 309.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/103946/mem-ria-hyperx-fury-8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3-8",
          "foto": "https://images6.kabum.com.br/produtos/fotos/103946/memoria-hyperx-fury-8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3-8_memoria-hyperx-fury-8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3-8_1567542849_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 103943,
          "nome": "Mem\u00f3ria HyperX Fury, 4GB, 2400MHz, DDR4, CL15, Preto - HX424C15FB3/4",
          "preco": 246.94,
          "preco_prime": 0.0,
          "preco_antigo": 305.76,
          "disponibilidade": "",
          "preco_desconto": 209.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/103943/mem-ria-hyperx-fury-4gb-2400mhz-ddr4-cl15-preto-hx424c15fb3-4",
          "foto": "https://images3.kabum.com.br/produtos/fotos/103943/memoria-hyperx-fury-4gb-2400mhz-ddr4-cl15-preto-hx424c15fb3-4_memoria-hyperx-fury-4gb-2400mhz-ddr4-cl15-preto-hx424c15fb3-4_1567534125_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 103947,
          "nome": "Mem\u00f3ria HyperX Fury, 16GB (2x8GB), 2400MHz, DDR4, CL15, Preto - HX424C15FB3K2/16",
          "preco": 748.12,
          "preco_prime": 0.0,
          "preco_antigo": 805.76,
          "disponibilidade": "",
          "preco_desconto": 635.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/103947/mem-ria-hyperx-fury-16gb-2x8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k2-16",
          "foto": "https://images7.kabum.com.br/produtos/fotos/103947/memoria-hyperx-fury-16gb-2x8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k2-16_memoria-hyperx-fury-16gb-2x8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k2-16_1567623521_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 103944,
          "nome": "Mem\u00f3ria HyperX Fury, 8GB (2x4GB), 2400MHz, DDR4, CL15, Preto - HX424C15FB3K2/8",
          "preco": 426.94,
          "preco_prime": 0.0,
          "preco_antigo": 435.18,
          "disponibilidade": "",
          "preco_desconto": 362.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/103944/mem-ria-hyperx-fury-8gb-2x4gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k2-8",
          "foto": "https://images4.kabum.com.br/produtos/fotos/103944/memoria-hyperx-fury-8gb-2x4gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k2-8_memoria-hyperx-fury-8gb-2x4gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k2-8_1567537606_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 103949,
          "nome": "Mem\u00f3ria HyperX Fury, 16GB, 2400MHz, DDR4, CL15, Preto - HX424C15FB3/16",
          "preco": 708.12,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 601.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/103949/mem-ria-hyperx-fury-16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3-16",
          "foto": "https://images9.kabum.com.br/produtos/fotos/103949/memoria-hyperx-fury-16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3-16_memoria-hyperx-fury-16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3-16_1567713407_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 104436,
          "nome": "Mem\u00f3ria HyperX Fury RGB, 8GB, 2400MHz, DDR4, CL15, Preto - HX424C15FB3A/8",
          "preco": 446.94,
          "preco_prime": 0.0,
          "preco_antigo": 459.88,
          "disponibilidade": "",
          "preco_desconto": 379.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/104436/mem-ria-hyperx-fury-rgb-8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3a-8",
          "foto": "https://images6.kabum.com.br/produtos/fotos/104436/memoria-hyperx-fury-rgb-8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3a-8_memoria-hyperx-fury-rgb-8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3a-8_1568832118_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 104439,
          "nome": "Mem\u00f3ria HyperX Fury RGB, 16GB, 2400MHz, DDR4, CL15, Preto - HX424C15FB3A/16",
          "preco": 772.82,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 656.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/104439/mem-ria-hyperx-fury-rgb-16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3a-16",
          "foto": "https://images9.kabum.com.br/produtos/fotos/104439/memoria-hyperx-fury-rgb-16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3a-16_memoria-hyperx-fury-rgb-16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3a-16_1568832436_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 104437,
          "nome": "Mem\u00f3ria HyperX Fury RGB, 16GB (2x8GB), 2400MHz, DDR4, CL15, Preto - HX424C15FB3AK2/16",
          "preco": 775.18,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 658.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/104437/mem-ria-hyperx-fury-rgb-16gb-2x8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3ak2-16",
          "foto": "https://images7.kabum.com.br/produtos/fotos/104437/memoria-hyperx-fury-rgb-16gb-2x8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3ak2-16_memoria-hyperx-fury-rgb-16gb-2x8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3ak2-16_1568836898_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 104440,
          "nome": "Mem\u00f3ria HyperX Fury RGB, 32GB (2x16GB), 2400MHz, DDR4, CL15, Preto - HX424C15FB3AK2/32",
          "preco": 1412.82,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 1200.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/104440/mem-ria-hyperx-fury-rgb-32gb-2x16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3ak2-32",
          "foto": "https://images0.kabum.com.br/produtos/fotos/104440/memoria-hyperx-fury-rgb-32gb-2x16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3ak2-32_memoria-hyperx-fury-rgb-32gb-2x16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3ak2-32_1568896986_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 103945,
          "nome": "Mem\u00f3ria HyperX Fury, 16GB (4x4GB), 2400MHz, DDR4, CL15, Preto - HX424C15FB3K4/16",
          "preco": 754.0,
          "preco_prime": 0.0,
          "preco_antigo": 872.82,
          "disponibilidade": "",
          "preco_desconto": 640.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/103945/mem-ria-hyperx-fury-16gb-4x4gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k4-16",
          "foto": "https://images5.kabum.com.br/produtos/fotos/103945/memoria-hyperx-fury-16gb-4x4gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k4-16_memoria-hyperx-fury-16gb-4x4gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k4-16_1567540925_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 103948,
          "nome": "Mem\u00f3ria HyperX Fury, 32GB (4x8GB), 2400MHz, DDR4, CL15, Preto - HX424C15FB3K4/32",
          "preco": 1514.0,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 1286.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/103948/mem-ria-hyperx-fury-32gb-4x8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k4-32",
          "foto": "https://images8.kabum.com.br/produtos/fotos/103948/memoria-hyperx-fury-32gb-4x8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k4-32_memoria-hyperx-fury-32gb-4x8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k4-32_1567624224_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 103950,
          "nome": "Mem\u00f3ria HyperX Fury, 32GB (2x16GB), 2400MHz, DDR4, CL15, Preto - HX424C15FB3K2/32",
          "preco": 1292.82,
          "preco_prime": 0.0,
          "preco_antigo": 1406.94,
          "disponibilidade": "",
          "preco_desconto": 1098.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/103950/mem-ria-hyperx-fury-32gb-2x16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k2-32",
          "foto": "https://images0.kabum.com.br/produtos/fotos/103950/memoria-hyperx-fury-32gb-2x16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k2-32_memoria-hyperx-fury-32gb-2x16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k2-32_1567627069_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 109768,
          "nome": "Mem\u00f3ria HyperX Fury, 128GB (4x32GB), 2400MHz, DDR4, CL15, Preto - HX424C15FB3K4/128",
          "preco": 5095.18,
          "preco_prime": 0.0,
          "preco_antigo": 5522.24,
          "disponibilidade": "",
          "preco_desconto": 4330.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/109768/mem-ria-hyperx-fury-128gb-4x32gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k4-128",
          "foto": "https://images8.kabum.com.br/produtos/fotos/109768/memoria-hyperx-fury-128gb-4x32gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k4-128_1580139571_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 104438,
          "nome": "Mem\u00f3ria HyperX Fury RGB, 32GB (4x8GB), 2400MHz, DDR4, CL15, Preto - HX424C15FB3AK4/32",
          "preco": 1552.82,
          "preco_prime": 0.0,
          "preco_antigo": 1614.0,
          "disponibilidade": "",
          "preco_desconto": 1319.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/104438/mem-ria-hyperx-fury-rgb-32gb-4x8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3ak4-32",
          "foto": "https://images8.kabum.com.br/produtos/fotos/104438/memoria-hyperx-fury-rgb-32gb-4x8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3ak4-32_memoria-hyperx-fury-rgb-32gb-4x8gb-2400mhz-ddr4-cl15-preto-hx424c15fb3ak4-32_1568892738_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 104441,
          "nome": "Mem\u00f3ria HyperX Fury RGB, 64GB (4x16GB), 2400MHz, DDR4, CL15, Preto - HX424C15FB3AK4/64",
          "preco": 3011.65,
          "preco_prime": 0.0,
          "preco_antigo": 3176.35,
          "disponibilidade": "",
          "preco_desconto": 2559.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/104441/mem-ria-hyperx-fury-rgb-64gb-4x16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3ak4-64",
          "foto": "https://images1.kabum.com.br/produtos/fotos/104441/memoria-hyperx-fury-rgb-64gb-4x16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3ak4-64_memoria-hyperx-fury-rgb-64gb-4x16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3ak4-64_1568893168_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 109766,
          "nome": "Mem\u00f3ria HyperX Fury, 32GB, 2400MHz, DDR4, CL15, Preto - HX424C15FB3/32",
          "preco": 1369.29,
          "preco_prime": 0.0,
          "preco_antigo": 1470.47,
          "disponibilidade": "",
          "preco_desconto": 1163.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/109766/mem-ria-hyperx-fury-32gb-2400mhz-ddr4-cl15-preto-hx424c15fb3-32",
          "foto": "https://images6.kabum.com.br/produtos/fotos/109766/memoria-hyperx-fury-32gb-2400mhz-ddr4-cl15-preto-hx424c15fb3-32_1579620552_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 109767,
          "nome": "Mem\u00f3ria HyperX Fury, 64GB (2x32GB), 2400MHz, DDR4, CL15, Preto - HX424C15FB3K2/64",
          "preco": 2689.29,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 2285.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/109767/mem-ria-hyperx-fury-64gb-2x32gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k2-64",
          "foto": "https://images7.kabum.com.br/produtos/fotos/109767/memoria-hyperx-fury-64gb-2x32gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k2-64_1580138784_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 103951,
          "nome": "Mem\u00f3ria HyperX Fury, 64GB (4x16GB), 2400MHz, DDR4, CL15, Preto - HX424C15FB3K4/64",
          "preco": 2341.06,
          "preco_prime": 0.0,
          "preco_antigo": 2352.82,
          "disponibilidade": "",
          "preco_desconto": 1989.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/103951/mem-ria-hyperx-fury-64gb-4x16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k4-64",
          "foto": "https://images1.kabum.com.br/produtos/fotos/103951/memoria-hyperx-fury-64gb-4x16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k4-64_memoria-hyperx-fury-64gb-4x16gb-2400mhz-ddr4-cl15-preto-hx424c15fb3k4-64_1567696449_m.jpg",
          "produto_prime": ""
        }
      ]
    },
    "fotos": [
      "https://images6.kabum.com.br/produtos/fotos/79936/79936_1520000156_g.jpg",
      "https://images6.kabum.com.br/produtos/fotos/79936/79936_index_g.jpg"
    ],
    "disponibilidade": "",
    "pre_venda": "",
    "fabricante": {
      "codigo": 1135,
      "nome": "Hyperx",
      "img": "https://images5.kabum.com.br/produtos/fabricantes/logo-hyperx.jpg"
    },
    "preco": 259.18,
    "preco_prime": 0.0,
    "preco_desconto": 220.3,
    "preco_desconto_prime": 0.0,
    "preco_antigo": 0.0,
    "economize_prime": 220.3,
    "descricao": "Solu\u00e7\u00e3o econ\u00f4mica a combina\u00e7\u00e3o perfeita de pre\u00e7o e desempenho DDR4, com exclusivo dissipador de calor assim\u00e9trico e com assinatura FURY possui um design de perfil baixo, dissipador de calor e PCB na cor preta.",
    "tag_title": "Mem\u00f3ria Kingston HyperX FURY 8GB | KaBuM!",
    "tem_frete_gratis": "",
    "frete_gratis_somente_prime": "",
    "tag_description": "Aproveite mem\u00f3ria HyperX FURY DDR4 no KaBuM! Compatibilidade com 90% das placas-m\u00e3es do mercado, parcelamento em at\u00e9 12x sem juros. Aproveite agora mesmo!",
    "avaliacao_numero": 894,
    "avaliacao_nota": 5,
    "desconto": 15,
    "is_openbox": "",
    "produto_html": "<p><span><span><span><strong>Caracter&iacute;sticas:</strong></span></span><br />- Marca: Kingston HyperX<br />- Modelo:&nbsp;HX424C15FB2/8<br /><strong><br /><span><span>Especifica&ccedil;&otilde;es:&nbsp;</span></span></strong><br />- Capacidade:&nbsp;</span><span>8GB</span><br /><span>- 2400Mhz</span><br /><span>-&nbsp;</span>DDR4-2400<br /><span>- Lat&ecirc;ncia:&nbsp;</span>15-15-15 at 1.2V<br /><span>-&nbsp;</span>DDR4-2400 CL15-15-15 @1.2V<br /><span>-&nbsp;288-Pin DIMM</span><br /><span>- Classifica&ccedil;&atilde;o UL: 94 V - 0</span><br /><span>- Temperatura de Opera&ccedil;&atilde;o: 0&ordm; C a +85&ordm; C&nbsp;</span><br /><span>- Temperatura de Armazenamento:&nbsp;-55&deg; C a +100&ordm; C</span><br /><br /><span><span><strong>Conte&uacute;do da Embalagem:</strong></span><br />- 01&nbsp;</span><span>Mem&oacute;ria Kingston HyperX FURY 8GB&nbsp;</span></p>",
    "dimensao_peso": 55,
    "peso": "55 gramas (bruto com embalagem)",
    "garantia": "1 ano de garantia",
    "codigo_anatel": "",
    "produto_especie": 0,
    "link_descricao": "/produto/79936/mem-ria-hyperx-fury-8gb-2400mhz-ddr4-cl15-preto-hx424c15fb2-8",
    "origem": "",
    "origem_nome": "",
    "flag_blackfriday": 0,
    "sucesso": ""
  },
  {
    "brinde": "",
    "oferta": "",
    "oferta_inicio": 0,
    "menus": [
      {
        "codigo": 1,
        "nome": "Hardware",
        "amigavel": "/hardware",
        "nome_url": "/Hardware"
      },
      {
        "codigo": 16,
        "nome": "Processadores",
        "amigavel": "/hardware/processadores",
        "nome_url": "/Hardware/Processadores"
      },
      {
        "codigo": 129,
        "nome": "AMD",
        "amigavel": "/hardware/processadores/amd",
        "nome_url": "/Hardware/Processadores/AMD"
      },
      {
        "codigo": 10497,
        "nome": "Ryzen",
        "amigavel": "/hardware/processadores/amd/ryzen",
        "nome_url": "/Hardware/Processadores/AMD/Ryzen"
      }
    ],
    "menu": "Hardware/Processadores/AMD/Ryzen",
    "codigo": 87400,
    "nome": "Processador AMD Ryzen 5 1600, Cooler Wraith Spire, Cache 19MB, 3.2GHz (3.6GHz Max Turbo), AM4, Sem V\u00eddeo - YD1600BBAEBOX",
    "familia": {
      "codigo": 0,
      "nome": "Amd",
      "titulo": "Fabricante",
      "produtos": [
        {
          "codigo": 107545,
          "nome": "Processador AMD Ryzen 5 1600, Cache 19MB, 3.2GHz (3.6GHz Max Turbo), AM4 - YD1600BBAFBOX",
          "preco": 870.47,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 739.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/107545/processador-amd-ryzen-5-1600-cache-19mb-3-2ghz-3-6ghz-max-turbo-am4-yd1600bbafbox",
          "foto": "https://images5.kabum.com.br/produtos/fotos/107545/processador-amd-ryzen-5-1600-cache-19mb-3-2ghz-3-6ghz-max-turbo-am4-yd1600bbafbox_1573653284_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 94723,
          "nome": "Processador AMD Ryzen 3 2200G, Cooler Wraith Stealth, Cache 6MB, 3.5GHz (3.7GHz Max Turbo), AM4 - YD2200C5FBBOX",
          "preco": 741.06,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 629.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/94723/processador-amd-ryzen-3-2200g-cooler-wraith-stealth-cache-6mb-3-5ghz-3-7ghz-max-turbo-am4-yd2200c5fbbox",
          "foto": "https://images3.kabum.com.br/produtos/fotos/94723/94723_1517918307_index_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 102437,
          "nome": "Processador AMD Ryzen 5 3600X Cache 32MB 3.8GHz (4.4GHz Max Turbo) AM4, Sem V\u00eddeo - 100-100000022BOX",
          "preco": 1764.59,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 1499.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/102437/processador-amd-ryzen-5-3600x-cache-32mb-3-8ghz-4-4ghz-max-turbo-am4-sem-v-deo-100-100000022box",
          "foto": "https://images7.kabum.com.br/produtos/fotos/102437/processador-amd-ryzen-5-3600x-cache-32mb-3-8ghz-4-4ghz-max-turbo-am4-100-100000022box_processador-amd-ryzen-5-3600x-cache-32mb-3-8ghz-4-4ghz-max-turbo-am4-100-100000022box_1562601561_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 95557,
          "nome": "Processador AMD Ryzen 5 2600, Cooler Wraith Stealth, Cache 19MB, 3.4GHz (3.9GHz Max Turbo), AM4, Sem V\u00eddeo - YD2600BBAFBOX",
          "preco": 1129.29,
          "preco_prime": 0.0,
          "preco_antigo": 1717.53,
          "disponibilidade": "",
          "preco_desconto": 959.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/95557/processador-amd-ryzen-5-2600-cooler-wraith-stealth-cache-19mb-3-4ghz-3-9ghz-max-turbo-am4-sem-v-deo-yd2600bbafbox",
          "foto": "https://images7.kabum.com.br/produtos/fotos/95557/95557_1522844873_index_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 102435,
          "nome": "Processador AMD Ryzen 7 3800X Cache 32MB 3.9GHz (4.5GHz Max Turbo) AMD4 - 100-100000025BOX",
          "preco": 3341.06,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 2839.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/102435/processador-amd-ryzen-7-3800x-cache-32mb-3-9ghz-4-5ghz-max-turbo-amd4-100-100000025box",
          "foto": "https://images5.kabum.com.br/produtos/fotos/102435/processador-amd-ryzen-7-3800x-cache-32mb-3-9ghz-4-5ghz-max-turbo-amd4-100-100000025box_processador-amd-ryzen-7-3800x-cache-32mb-3-9ghz-4-5ghz-max-turbo-amd4-100-100000025box_1562600416_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 113391,
          "nome": "Processador AMD Ryzen 3 3300X, Cache 18MB, 4.3Ghz, AM4 - 100-100000159BOX",
          "preco": 1141.06,
          "preco_prime": 0.0,
          "preco_antigo": 1152.82,
          "disponibilidade": "",
          "preco_desconto": 969.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/113391/processador-amd-ryzen-3-3300x-cache-18mb-4-3ghz-am4-100-100000159box",
          "foto": "https://images1.kabum.com.br/produtos/fotos/113391/processador-amd-ryzen-3-3300x-cache-18mb-4-3ghz-am4-100-100000159box_1590062995_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 102436,
          "nome": "Processador AMD Ryzen 7 3700X 32MB 3.6GHz (4.4GHz Max Turbo) AM4, Sem V\u00eddeo - 100-100000071BOX",
          "preco": 2875.18,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 2443.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/102436/processador-amd-ryzen-7-3700x-32mb-3-6ghz-4-4ghz-max-turbo-am4-sem-v-deo-100-100000071box",
          "foto": "https://images6.kabum.com.br/produtos/fotos/102436/processador-amd-ryzen-7-3700x-32mb-3-6ghz-4-6ghz-max-turbo-amd4-100-100000071box_processador-amd-ryzen-7-3700x-32mb-3-6ghz-4-6ghz-max-turbo-amd4-100-100000071box_1562601118_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 102434,
          "nome": "Processador AMD Ryzen 9 3900X Cache 64MB 3.8GHz (4.6GHz Max Turbo) AM4, Sem V\u00eddeo - 100-100000023BOX",
          "preco": 4270.47,
          "preco_prime": 0.0,
          "preco_antigo": 4665.76,
          "disponibilidade": "",
          "preco_desconto": 3629.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/102434/processador-amd-ryzen-9-3900x-cache-64mb-3-8ghz-4-6ghz-max-turbo-am4-sem-v-deo-100-100000023box",
          "foto": "https://images4.kabum.com.br/produtos/fotos/102434/processador-amd-ryzen-9-3900x-cache-64mb-3-8ghz-4-6ghz-max-turbo-amd4-100-100000023box_processador-amd-ryzen-9-3900x-cache-64mb-3-8ghz-4-6ghz-max-turbo-amd4-100-100000023box_1562599455_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 95563,
          "nome": "Processador AMD Ryzen 5 2600X, Cooler Wraith Spire, Cache 19MB, 3.6GHz (4.25GHz Max Turbo), AM4, Sem V\u00eddeo - YD260XBCAFBOX",
          "preco": 1717.53,
          "preco_prime": 0.0,
          "preco_antigo": 1839.88,
          "disponibilidade": "",
          "preco_desconto": 1459.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/95563/processador-amd-ryzen-5-2600x-cooler-wraith-spire-cache-19mb-3-6ghz-4-25ghz-max-turbo-am4-sem-v-deo-yd260xbcafbox",
          "foto": "https://images3.kabum.com.br/produtos/fotos/95563/95563_1522844766_index_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 114265,
          "nome": "Processador AMD Ryzen 7 3800XT, Cache 36MB, 3.8GHz (4.7GHz Max Turbo), AM4 - 100-100000279WOF",
          "preco": 3646.94,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 3099.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/114265/processador-amd-ryzen-7-3800xt-cache-36mb-3-8ghz-4-7ghz-max-turbo-am4-100-100000279wof",
          "foto": "https://images5.kabum.com.br/produtos/fotos/114265/processador-amd-ryzen-7-3800xt-cache-36mb-4700mhz-am4-100-100000279wof_1594061933_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 114266,
          "nome": "Processador AMD Ryzen 5 3600XT, Cache 35MB, 3.8GHz (4.5GHz Max Turbo), AM4 - 100-100000281BOX",
          "preco": 2282.24,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 1939.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/114266/processador-amd-ryzen-5-3600xt-cache-35mb-3-8ghz-4-5ghz-max-turbo-am4-100-100000281box",
          "foto": "https://images6.kabum.com.br/produtos/fotos/114266/processador-amd-ryzen-5-3600xt-cache-35mb-4500mhz-am4-100-100000281box_1594062940_m.jpg",
          "produto_prime": ""
        },
        {
          "codigo": 114264,
          "nome": "Processador AMD Ryzen 9 3900XT, Cache 70MB, 4700MHz, AM4 - 100-100000277WOF",
          "preco": 4588.12,
          "preco_prime": 0.0,
          "preco_antigo": 0.0,
          "disponibilidade": "",
          "preco_desconto": 3899.9,
          "preco_desconto_prime": 0.0,
          "link_descricao": "/produto/114264/processador-amd-ryzen-9-3900xt-cache-70mb-4700mhz-am4-100-100000277wof",
          "foto": "https://images4.kabum.com.br/produtos/fotos/114264/processador-amd-ryzen-9-3900xt-cache-70mb-4700mhz-am4-100-100000277wof_1594061535_m.jpg",
          "produto_prime": ""
        }
      ]
    },
    "fotos": [
      "https://images0.kabum.com.br/produtos/fotos/87400/87400_1489773805_g.jpg",
      "https://images0.kabum.com.br/produtos/fotos/87400/87400_index_g.jpg"
    ],
    "disponibilidade": "",
    "pre_venda": "",
    "fabricante": {
      "codigo": 5,
      "nome": "Amd",
      "img": "https://images5.kabum.com.br/produtos/fabricantes/logo-amd.jpg"
    },
    "preco": 788.12,
    "preco_prime": 0.0,
    "preco_desconto": 669.9,
    "preco_desconto_prime": 0.0,
    "preco_antigo": 0.0,
    "economize_prime": 669.9,
    "descricao": "Com esse processador inovador e incr\u00edvel voc\u00ea desfruta ao m\u00e1ximo o verdadeiro potencial do seu computador e desfruta da mais pura velocidade. Maximize o seu desempenho seja trabalhando, jogando, navegando ou assistindo o seu filme preferido, com esse processador voc\u00ea pode tudo!",
    "tag_title": "Processador AMD Ryzen 5 1600, Cooler Wraith Spire | KaBuM!",
    "tem_frete_gratis": "",
    "frete_gratis_somente_prime": "",
    "tag_description": "Aproveite Processador AMD Ryzen 5 1600 no KaBuM! Max Turbo 3.6GHz, 12 Threads, Pot\u00eancia 65 W, Parcelamento at\u00e9 12x Sem Juros! Compre Agora Mesmo",
    "avaliacao_numero": 313,
    "avaliacao_nota": 5,
    "desconto": 15,
    "is_openbox": "",
    "produto_html": "<table style=\"width: 720;\" border=\"0\"><tbody><tr><td><p style=\"text-align: center;\"><img src=\"https://images0.kabum.com.br/produtos/fotos/87400/conteudo/878157aviso-new.jpg\" alt=\"\" width=\"720\" height=\"294\" /></p></td></tr></tbody></table><table style=\"width: 720px; height: 1519px; text-align: left;\" border=\"0\" background=\"https://images0.kabum.com.br/produtos/fotos/87400/conteudo/797427bkgd-1600.jpg\"><tbody><tr><td valign=\"top\"><br /><h1 style=\"margin-top: 145px; text-align: center;\"><iframe src=\"https://www.youtube.com/embed/tNldks6AR4Q?rel=0&amp;showinfo=0\" width=\"700\" height=\"402\"></iframe></h1><br /><p style=\"font-family: 'Myriad Pro','Gill Sans', 'Gill Sans MT', 'DejaVu Sans Condensed', Helvetica, Arial, sans-serif; font-size: 16px; color: #fff; text-align:justify; padding:1em; margin-left:200px; margin-top: 740px;\">Jogos eficientes e sem interrup&ccedil;&otilde;es e desenvolvimento de <br />multi-processamento</p><br /><p style=\"font-family: 'Myriad Pro','Gill Sans', 'Gill Sans MT', 'DejaVu Sans Condensed', Helvetica, Arial, sans-serif; font-size: 16px; color: #fff; text-align:justify; padding:1em; margin-left:200px; margin-top: -30px;\">- Taxa de clock de 3,2 GHz com Precision Boost de 3,6 GHz <br /> - Cooler AMD Wraith Spire&nbsp;<br /> - TDP (projeto de for&ccedil;a t&eacute;rmica) de 65 Watts</p><p style=\"font-family: 'Myriad Pro','Gill Sans', 'Gill Sans MT', 'DejaVu Sans Condensed', Helvetica, Arial, sans-serif; font-size: 16px; color: #fff; text-align:justify; padding:1em; margin-left:200px; margin-top: -30px;\">&nbsp;</p></td></tr></tbody></table><table style=\"width: 720px;\" border=\"0\"><tbody><tr><td><p style=\"text-align: center;\"><img src=\"https://images0.kabum.com.br/produtos/fotos/87400/conteudo/876303separa.jpg\" alt=\"\" width=\"709\" height=\"27\" /></p></td></tr></tbody></table><p><strong>Caracter&iacute;sticas:</strong></p><p>- Marca: AMD</p><p>- Modelo: YD1600BBAEBOX</p><p>&nbsp;</p><p><strong>Especifica&ccedil;&otilde;es:</strong></p><p>- S&eacute;ries: Ryzen 5</p><p>- Processo de fabrica&ccedil;&atilde;o: 14nm</p><p>- Socket: Socket AM4</p><p>- N&uacute;cleos: 6 core</p><p>- Threads: 12</p><p>- Frequ&ecirc;ncia de Opera&ccedil;&atilde;o: 3.2GHz (Max Turbo 3.6GHz)</p><p>- Cache L3: 16MB</p><p>- Cache L2: 3MB</p><p>- Modo de opera&ccedil;&atilde;o: 64 Bit</p><p>- Pot&ecirc;ncia: 65 W&nbsp;</p><p>&nbsp;</p><p><strong>Conte&uacute;do da Embalagem:</strong></p><p>- 01 Processador AMD&nbsp;</p><p>- 01 Cooler</p><p>&nbsp;</p><p><strong>Observa&ccedil;&atilde;o:</strong></p><p><em>* As linhas de processadores Ryzen 3, 5 e 7 n&atilde;o possuem v&iacute;deo integrado, necess&aacute;rio ter uma placa de v&iacute;deo off-board.</em></p><p>&nbsp;</p><p><em><strong>ESTE PROCESSADOR N&Atilde;O POSSUI V&Iacute;DEO INTEGRADO!</strong></em></p><p><em><strong><br /></strong></em></p><p><em><strong><em></em></strong></em></p><p><em><strong>* Fiquei Ligado: Para montar um setup com esse modelo de processador, &eacute; necess&aacute;rio a instala&ccedil;&atilde;o de uma placa de v&iacute;deo, pois o mesmo n&atilde;o possui v&iacute;deo integrado.</strong></em></p>",
    "dimensao_peso": 665,
    "peso": "665 gramas (bruto com embalagem)",
    "garantia": "1 ano de garantia",
    "codigo_anatel": "",
    "produto_especie": 0,
    "link_descricao": "/produto/87400/processador-amd-ryzen-5-1600-cooler-wraith-spire-cache-19mb-3-2ghz-3-6ghz-max-turbo-am4-sem-v-deo-yd1600bbaebox",
    "origem": "",
    "origem_nome": "",
    "flag_blackfriday": 0,
    "sucesso": ""
  }
]

class Products(Resource):
    def get(self):
        return {'Product':products}

class Product(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('preco')
    argumentos.add_argument('nome')

    def find_product(codigo):
        print(codigo)
        for x in products:
            if x['codigo'] == codigo:
                return x
        return None

    def get(self, codigo):
        prod = Product.find_product(codigo)
        if prod:
            return prod
        return {'message': 'Produto not found'}, 404  # not found

    def post(self, codigo):

        if Product.find_product(codigo):
            return {"message":"Codigo '{}' alredy existis." .format(codigo)}, 400 # Bad Request

        dados = Product.argumentos.parse_args()
        product_object = ProductModel(codigo, **dados)
        new_product = product_object.json()

        try:
            products.append(new_product)
        except:
            return {'messege': 'An internal error ocurred trying to save produto'}, 500 # An server error
        return new_product, 200

    def put(self, codigo):
        dados = Product.argumentos.parse_args()
        product_object = ProductModel(codigo, **dados)
        new_product = product_object.json()
        prod = Product.find_product(codigo)
        if prod:
            prod.update(new_product)
            return new_product, 200
        try:
          products.append(new_product)
        except:
          return {'messege': 'An internal error ocurred trying to save produto'}, 500  # An server error
        return new_product, 200

    def delete(self, codigo):
      prod = Product.find_product(codigo)
      if prod:
        try:
          products.remove(prod)
        except:
          return {'message': 'An error ocurred trying to delete produto'}, 500  # An server error
        return {'message': 'Produto Deleted.'}
      return {'messege': 'Produto not found.'}, 404
