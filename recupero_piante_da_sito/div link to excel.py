from bs4 import BeautifulSoup
import pandas as pd
link="""https://tropica.com//en/plants/plantdetails/Aegagropilalinnaei(000CST)/4385
https://tropica.com//en/plants/plantdetails/Aegagropilalinnaei(000DMP)/19534
https://tropica.com//en/plants/plantdetails/Alternantherareineckii'Mini'(023CTC)/4439
https://tropica.com//en/plants/plantdetails/Alternantherareineckii'Pink'(023XL)/4437
https://tropica.com//en/plants/plantdetails/Alternantherareineckii'Pink'(023)/4436
https://tropica.com//en/plants/plantdetails/Alternantherareineckii'Rosanervig'(023D)/4440
https://tropica.com//en/plants/plantdetails/Ammanniacrassicaulis(033B)/4449
https://tropica.com//en/plants/plantdetails/Anubiasbarteri’CoinLeaf’(101F)/29447
https://tropica.com//en/plants/plantdetails/Anubiasbartericaladiifolia(101UPCS)/18816
https://tropica.com//en/plants/plantdetails/Anubiasbarteri'MiniCoin'(101BTC)/28816
https://tropica.com//en/plants/plantdetails/Anubiasbarterinana(101TC)/18895
https://tropica.com//en/plants/plantdetails/Anubiasbarteri'Petite'(101H)/4554
https://tropica.com//en/plants/plantdetails/Anubiasbarterisp.(101YWX)/4549
https://tropica.com//en/plants/plantdetails/Anubiasbarterivar.barteri(101A)/4551
https://tropica.com//en/plants/plantdetails/Anubiasbarterivar.caladiifolia(101UXL)/4557
https://tropica.com//en/plants/plantdetails/Anubiasbarterivar.caladiifolia(101U)/4556
https://tropica.com//en/plants/plantdetails/Anubiasbarterivar.'Coffeifolia'(101G)/4553
https://tropica.com//en/plants/plantdetails/Anubiasbarterivar.glabra(101C)/4552
https://tropica.com//en/plants/plantdetails/Anubiasbarterivar.nana(101PCS)/18806
https://tropica.com//en/plants/plantdetails/Anubiasbarterivar.nana(101YLS)/4546
https://tropica.com//en/plants/plantdetails/Anubiasbarterivar.nana(101YWS)/4548
https://tropica.com//en/plants/plantdetails/Anubiasbarterivar.nana(101ZWS)/4550
https://tropica.com//en/plants/plantdetails/Anubiasbarterivar.nana(101)/4545
https://tropica.com//en/plants/plantdetails/Anubiasbarterivar.nana(510YCS)/28184
https://tropica.com//en/plants/plantdetails/Anubiasbarterivar.nana’Kirin’(101K)/29448
https://tropica.com//en/plants/plantdetails/Anubiasbarterivar.nana’Pinto’(101E)/29446
https://tropica.com//en/plants/plantdetails/Anubiasbarterivar.nana'Large'(101L)/19785
https://tropica.com//en/plants/plantdetails/Anubiasgracilis(101D)/17819
https://tropica.com//en/plants/plantdetails/Aponogetonboivinianus(088KN)/4534
https://tropica.com//en/plants/plantdetails/Aponogetonlongiplumulosus(089DKN)/4536
https://tropica.com//en/plants/plantdetails/Aponogetonmadagascariensis(089KN)/4535
https://tropica.com//en/plants/plantdetails/Aponogetonulvaceus(086KN)/4533
https://tropica.com//en/plants/plantdetails/Bacopaaustralis(043A)/4466
https://tropica.com//en/plants/plantdetails/Bacopacaroliniana(043BDT)/4465
https://tropica.com//en/plants/plantdetails/Bacopacaroliniana(043MP)/18811
https://tropica.com//en/plants/plantdetails/Bacopacaroliniana(043TC)/18752
https://tropica.com//en/plants/plantdetails/Bacopacaroliniana(043)/4464
https://tropica.com//en/plants/plantdetails/Bacopamonnieri'Compact'(044APCS)/18800
https://tropica.com//en/plants/plantdetails/Bacopamonnieri'Compact'(044A)/4467
https://tropica.com//en/plants/plantdetails/Blyxajaponica(057TC)/22542
https://tropica.com//en/plants/plantdetails/Bolbitisheudelotii(006XL)/18376
https://tropica.com//en/plants/plantdetails/Bolbitisheudelotii(006YWS)/4407
https://tropica.com//en/plants/plantdetails/Bolbitisheudelotii(006)/4406
https://tropica.com//en/plants/plantdetails/Bucephalandra'Kedagang'(139BTC)/22544
https://tropica.com//en/plants/plantdetails/Bucephalandra'Kedagang'(139B)/22543
https://tropica.com//en/plants/plantdetails/Bucephalandrapygmaea'BukitKelam'(139TC)/28393
https://tropica.com//en/plants/plantdetails/Bucephalandrapygmaea'BukitKelam'(139)/18757
https://tropica.com//en/plants/plantdetails/Bucephalandrapygmaea'WavyGreen'(139YLS)/18758
https://tropica.com//en/plants/plantdetails/Bucephalandrasp.'NeedleLeaf'(139CTC)/29517
https://tropica.com//en/plants/plantdetails/Bucephalandrasp.'Red'(139A)/19682
https://tropica.com//en/plants/plantdetails/Cabombaaquatica(015BDT)/4431
https://tropica.com//en/plants/plantdetails/Cardaminelyrata(024)/4441
https://tropica.com//en/plants/plantdetails/Ceratophyllumdemersum(021APOR)/4434
https://tropica.com//en/plants/plantdetails/Ceratopteristhalictroides(005A)/4405
https://tropica.com//en/plants/plantdetails/Crinumcalamistratum(094A)/4541
https://tropica.com//en/plants/plantdetails/Crinumthaianum(093)/4537
https://tropica.com//en/plants/plantdetails/Cryptocorynealbida'Brown'(126B)/18194
https://tropica.com//en/plants/plantdetails/Cryptocorynebeckettii'Petchii'(108APCS)/18807
https://tropica.com//en/plants/plantdetails/Cryptocorynebeckettii'Petchii'(108AYLS)/4561
https://tropica.com//en/plants/plantdetails/Cryptocorynebeckettii'Petchii'(108A)/4560
https://tropica.com//en/plants/plantdetails/Cryptocorynecrispatula(125TC)/18756
https://tropica.com//en/plants/plantdetails/Cryptocorynecrispatula(125)/4567
https://tropica.com//en/plants/plantdetails/Cryptocorynenurii(126TC)/29518
https://tropica.com//en/plants/plantdetails/Cryptocoryneparva(106TC)/18755
https://tropica.com//en/plants/plantdetails/Cryptocoryneparva(106)/4558
https://tropica.com//en/plants/plantdetails/Cryptocoryneundulata'BroadLeaf'(110A)/4566
https://tropica.com//en/plants/plantdetails/Cryptocoryneundulata'BroadLeaf'(110BTC)/19225
https://tropica.com//en/plants/plantdetails/Cryptocoryneusteriana(120)/18405
https://tropica.com//en/plants/plantdetails/Cryptocorynewendtii'Green'(109TC)/19226
https://tropica.com//en/plants/plantdetails/Cryptocorynewendtii'Green'(109)/4562
https://tropica.com//en/plants/plantdetails/Cryptocorynewendtii'MiOya'(109DTC)/19540
https://tropica.com//en/plants/plantdetails/Cryptocorynewendtii'Tropica'(109EXL)/4565
https://tropica.com//en/plants/plantdetails/Cryptocorynewendtii'Tropica'(109E)/4564
https://tropica.com//en/plants/plantdetails/Cryptocorynexwillisii(107PCS)/19618
https://tropica.com//en/plants/plantdetails/Cryptocorynexwillisii(107)/4559
https://tropica.com//en/plants/plantdetails/Cyperushelferi(133A)/4574
https://tropica.com//en/plants/plantdetails/Echinodorus'Aquartica'(074F)/4526
https://tropica.com//en/plants/plantdetails/Echinodoruscordifolius'Fluitans'(073D)/4519
https://tropica.com//en/plants/plantdetails/Echinodorusgrisebachii'Bleherae'(071BDT)/4513
https://tropica.com//en/plants/plantdetails/Echinodorusgrisebachii'Bleherae'(071XL)/21211
https://tropica.com//en/plants/plantdetails/Echinodorusgrisebachii'Bleherae'(071)/4512
https://tropica.com//en/plants/plantdetails/Echinodorus'Ozelot'(073FXL)/4521
https://tropica.com//en/plants/plantdetails/Echinodorus'Ozelot'(073F)/4520
https://tropica.com//en/plants/plantdetails/Echinodorus'OzelotGreen'(073G)/4522
https://tropica.com//en/plants/plantdetails/Echinodoruspalifolius(076XL)/4528
https://tropica.com//en/plants/plantdetails/Echinodoruspalifolius(076)/4527
https://tropica.com//en/plants/plantdetails/Echinodorus'RedDiamond'(074D)/4525
https://tropica.com//en/plants/plantdetails/Echinodorus'Reni'(072DPCS)/18818
https://tropica.com//en/plants/plantdetails/Echinodorus'Reni'(072DTC)/18754
https://tropica.com//en/plants/plantdetails/Echinodorus'Reni'(072D)/4518
https://tropica.com//en/plants/plantdetails/Echinodorus'Rosé'(072BXL)/4517
https://tropica.com//en/plants/plantdetails/Echinodorus'Rosé'(072B)/4516
https://tropica.com//en/plants/plantdetails/Echinodorusxbarthii(072AXL)/4515
https://tropica.com//en/plants/plantdetails/Echinodorusxbarthii(072A)/4514
https://tropica.com//en/plants/plantdetails/Egeriadensa(058BDT)/4506
https://tropica.com//en/plants/plantdetails/Elatinehydropiper(141TC)/18759
https://tropica.com//en/plants/plantdetails/Eleocharisacicularis(133TC)/28401
https://tropica.com//en/plants/plantdetails/Eleocharismontevidensis(132D)/4573
https://tropica.com//en/plants/plantdetails/Eleocharisparvula(132C)/4572
https://tropica.com//en/plants/plantdetails/Eleocharispusilla'Mini'(132BTC)/4571
https://tropica.com//en/plants/plantdetails/Eriocauloncinereum(091TC)/19547
https://tropica.com//en/plants/plantdetails/Fissidensfontanus(002F)/4390
https://tropica.com//en/plants/plantdetails/Glossostigmaelatinoides(045ATC)/4470
https://tropica.com//en/plants/plantdetails/Gratiolaviscidula(042TC)/18390
https://tropica.com//en/plants/plantdetails/Helanthiumbolivianum'Quadricostatus'(068TC)/18896
https://tropica.com//en/plants/plantdetails/Helanthiumbolivianum'Quadricostatus'(068)/4511
https://tropica.com//en/plants/plantdetails/Helanthiumtenellum'Green'(067ATC)/4757
https://tropica.com//en/plants/plantdetails/Hemianthusmicranthemoides(048ATC)/22879
https://tropica.com//en/plants/plantdetails/Heterantherazosterifolia(096TC)/4544
https://tropica.com//en/plants/plantdetails/Hottoniapalustris(027TC)/28508
https://tropica.com//en/plants/plantdetails/Hottoniapalustris(027)/4443
https://tropica.com//en/plants/plantdetails/Hydrocotyletripartita(039BTC)/18751
https://tropica.com//en/plants/plantdetails/Hydrocotyletripartita(039B)/4458
https://tropica.com//en/plants/plantdetails/Hydrocotyleverticillata(039)/4457
https://tropica.com//en/plants/plantdetails/Hygrophilacorymbosa(053BDT)/4490
https://tropica.com//en/plants/plantdetails/Hygrophilacorymbosa'Compact'(052D)/18774
https://tropica.com//en/plants/plantdetails/Hygrophilacorymbosa'Siamensis53B'(053BMP)/18813
https://tropica.com//en/plants/plantdetails/Hygrophilacorymbosa'Siamensis53B'(053BPCS)/18803
https://tropica.com//en/plants/plantdetails/Hygrophilacorymbosa'Siamensis53B'(053B)/4493
https://tropica.com//en/plants/plantdetails/Hygrophilacorymbosa'Stricta'(053AXL)/4492
https://tropica.com//en/plants/plantdetails/Hygrophilacorymbosa'Stricta'(053A)/4491
https://tropica.com//en/plants/plantdetails/Hygrophilacostata(052A)/4489
https://tropica.com//en/plants/plantdetails/Hygrophiladifformis(051BDT)/4485
https://tropica.com//en/plants/plantdetails/Hygrophilalancea'Araguaia'(051BTC)/4758
https://tropica.com//en/plants/plantdetails/Hygrophilapinnatifida(051ATC)/19228
https://tropica.com//en/plants/plantdetails/Hygrophilapinnatifida(051A)/4486
https://tropica.com//en/plants/plantdetails/Hygrophilapinnatifida(509YCS)/28279
https://tropica.com//en/plants/plantdetails/Hygrophilapinnatifidaandmoss(051AYWS)/4487
https://tropica.com//en/plants/plantdetails/Hygrophilapolysperma(050)/4483
https://tropica.com//en/plants/plantdetails/Hygrophilapolysperma'Rosanervig'(050B)/4484
https://tropica.com//en/plants/plantdetails/Juncusrepens   (133FTC)/28107
https://tropica.com//en/plants/plantdetails/Lagenandrameeboldii'Red'(103)/4759
https://tropica.com//en/plants/plantdetails/Leptodictyumriparium(003ETC)/28671
https://tropica.com//en/plants/plantdetails/Lilaeopsisbrasiliensis(040PCS)/18808
https://tropica.com//en/plants/plantdetails/Lilaeopsisbrasiliensis(040TC)/4460
https://tropica.com//en/plants/plantdetails/Lilaeopsisbrasiliensis(040)/4459
https://tropica.com//en/plants/plantdetails/Limnobiumlaevigatum(063TC)/4761
https://tropica.com//en/plants/plantdetails/Limnophilaaquatica(046)/4471
https://tropica.com//en/plants/plantdetails/Limnophilahippuridoides(047C)/4474
https://tropica.com//en/plants/plantdetails/Limnophilasessiliflora(047MP)/18812
https://tropica.com//en/plants/plantdetails/Limnophilasessiliflora(047PCS)/18801
https://tropica.com//en/plants/plantdetails/Limnophilasessiliflora(047)/4472
https://tropica.com//en/plants/plantdetails/Linderniarotundifolia(045)/4468
https://tropica.com//en/plants/plantdetails/Littorellauniflora(081TC)/18269
https://tropica.com//en/plants/plantdetails/Lobeliacardinalis(053CMP)/18840
https://tropica.com//en/plants/plantdetails/Lobeliacardinalis(053CPCS)/21134
https://tropica.com//en/plants/plantdetails/Lobeliacardinalis(053C)/4494
https://tropica.com//en/plants/plantdetails/Lobeliacardinalis'Mini'(143TC)/28647
https://tropica.com//en/plants/plantdetails/Ludwigiaglandulosa(035A)/4452
https://tropica.com//en/plants/plantdetails/Ludwigiapalustris'SuperRed'(035B)/4453
https://tropica.com//en/plants/plantdetails/Ludwigiarepens'Rubin'(033D)/4450
https://tropica.com//en/plants/plantdetails/Marsileahirsuta(010TC)/4428
https://tropica.com//en/plants/plantdetails/Marsileaminuta(010BTC)/4762
https://tropica.com//en/plants/plantdetails/Mayacafluviatilis(140BDT)/19792
https://tropica.com//en/plants/plantdetails/Micranthemumcallitrichoides´Cuba´(048B)/4477
https://tropica.com//en/plants/plantdetails/Micranthemumcallitrichoides'Cuba'(048BTC)/4478
https://tropica.com//en/plants/plantdetails/Micranthemumglomeratum(048A)/4476
https://tropica.com//en/plants/plantdetails/Micranthemumtweediei'MonteCarlo'(025TC)/4442
https://tropica.com//en/plants/plantdetails/Micranthemumtweediei'MonteCarlo'(025)/22880
https://tropica.com//en/plants/plantdetails/Micranthemumumbrosum(048ST)/19793
https://tropica.com//en/plants/plantdetails/Micranthemumumbrosum(048)/4475
https://tropica.com//en/plants/plantdetails/Microsorum-Anubias'Duet'(008NYWX)/4427
https://tropica.com//en/plants/plantdetails/Microsorumpteropus(008XL)/4409
https://tropica.com//en/plants/plantdetails/Microsorumpteropus(008YLS)/4410
https://tropica.com//en/plants/plantdetails/Microsorumpteropus(008YWS)/4412
https://tropica.com//en/plants/plantdetails/Microsorumpteropus(008YWX)/4413
https://tropica.com//en/plants/plantdetails/Microsorumpteropus(008)/4408
https://tropica.com//en/plants/plantdetails/Microsorumpteropus'Narrow'(008APCS)/18821
https://tropica.com//en/plants/plantdetails/Microsorumpteropus'Narrow'(008AYWS)/4415
https://tropica.com//en/plants/plantdetails/Microsorumpteropus'Narrow'(008AZWS)/4417
https://tropica.com//en/plants/plantdetails/Microsorumpteropus'Narrow'(008A)/4414
https://tropica.com//en/plants/plantdetails/Microsorumpteropus'Trident'(008GYWS)/4425
https://tropica.com//en/plants/plantdetails/Microsorumpteropus'Trident'(008GZWM)/4426
https://tropica.com//en/plants/plantdetails/Microsorumpteropus'Trident'(008GZWS)/19275
https://tropica.com//en/plants/plantdetails/Microsorumpteropus'Trident'(008G)/4424
https://tropica.com//en/plants/plantdetails/Microsorumpteropus'Windeløv'(008BYWS)/4420
https://tropica.com//en/plants/plantdetails/Microsorumpteropus'Windeløv'(008BYWX)/4421
https://tropica.com//en/plants/plantdetails/Microsorumpteropus'Windeløv'(008BZWM)/4422
https://tropica.com//en/plants/plantdetails/Microsorumpteropus'Windeløv'(008BZWS)/4423
https://tropica.com//en/plants/plantdetails/Microsorumpteropus'Windeløv'(008B)/4418
https://tropica.com//en/plants/plantdetails/Microsorumsp.(500OWX)/4582
https://tropica.com//en/plants/plantdetails/Monosoleniumtenerum(002CTC)/18747
https://tropica.com//en/plants/plantdetails/Murdanniakeisak(135)/4763
https://tropica.com//en/plants/plantdetails/Myriophyllummattogrossense(037TC)/28108
https://tropica.com//en/plants/plantdetails/Myriophyllummattogrossense(037)/4454
https://tropica.com//en/plants/plantdetails/Myriophyllumsp.'Guyana'(037ETC)/19549
https://tropica.com//en/plants/plantdetails/Nymphaealotus(019)/4432
https://tropica.com//en/plants/plantdetails/Nymphoideshydrophylla'Taiwan'(041BTC)/4463
https://tropica.com//en/plants/plantdetails/Nymphoideshydrophylla'Taiwan'(041B)/4462
https://tropica.com//en/plants/plantdetails/Phyllanthusfluitans(028TC)/22848
https://tropica.com//en/plants/plantdetails/Pogostemondeccanensis(053FTC)/4497
https://tropica.com//en/plants/plantdetails/Pogostemondeccanensis(053F)/4496
https://tropica.com//en/plants/plantdetails/Pogostemonhelferi(053HTC)/19680
https://tropica.com//en/plants/plantdetails/Pogostemonhelferi(053HYLS)/4500
https://tropica.com//en/plants/plantdetails/Pogostemonhelferi(053H)/4499
https://tropica.com//en/plants/plantdetails/Pogostemonstellatus(053G)/4498
https://tropica.com//en/plants/plantdetails/Proserpinacapalustris'Cuba'(037CTC)/4766
https://tropica.com//en/plants/plantdetails/Ranunculusinundatus(022CTC)/18225
https://tropica.com//en/plants/plantdetails/Riccardiachamedryfolia(003D)/4400
https://tropica.com//en/plants/plantdetails/Ricciafluitans(001TC)/4386
https://tropica.com//en/plants/plantdetails/Rotalaindica'Bonsai'(033ETC)/4451
https://tropica.com//en/plants/plantdetails/Rotalamacrandra(032TC)/4445
https://tropica.com//en/plants/plantdetails/Rotalarotundifolia(033MP)/18810
https://tropica.com//en/plants/plantdetails/Rotalarotundifolia(033PCS)/18799
https://tropica.com//en/plants/plantdetails/Rotalarotundifolia(033)/4447
https://tropica.com//en/plants/plantdetails/Rotalarotundifolia'Green'(033ATC)/22545
https://tropica.com//en/plants/plantdetails/Rotalarotundifolia'H'ra'(032CTC)/19550
https://tropica.com//en/plants/plantdetails/Rotalawallichii(032ATC)/18748
https://tropica.com//en/plants/plantdetails/Sagittariasubulata(079PCS)/21135
https://tropica.com//en/plants/plantdetails/Sagittariasubulata(079TC)/18270
https://tropica.com//en/plants/plantdetails/Sagittariasubulata(079)/4530
https://tropica.com//en/plants/plantdetails/Schismatoglottisprietoi(102TC)/29519
https://tropica.com//en/plants/plantdetails/Shinnersiarivularis'Weiss-Grün'(053E)/4495
https://tropica.com//en/plants/plantdetails/Staurogynerepens(049GPCS)/19617
https://tropica.com//en/plants/plantdetails/Staurogynerepens(049GTC)/4482
https://tropica.com//en/plants/plantdetails/Staurogynerepens(049G)/4481
https://tropica.com//en/plants/plantdetails/Taxiphyllumalternans'TaiwanMoss'(003CTC)/19551
https://tropica.com//en/plants/plantdetails/Taxiphyllumbarbieri'BogorMoss'(003POR)/4391
https://tropica.com//en/plants/plantdetails/Taxiphyllumbarbieri'BogorMoss'(003TC)/4393
https://tropica.com//en/plants/plantdetails/Taxiphyllumbarbieri'BogorMoss'(003YLS)/4394
https://tropica.com//en/plants/plantdetails/Taxiphyllumsp.’FlameMoss’(003HTC)/4403
https://tropica.com//en/plants/plantdetails/Taxiphyllumsp.'SpikyMoss'(003GPOR)/4402
https://tropica.com//en/plants/plantdetails/Taxiphyllumsp.'SpikyMoss'(003GTC)/18271
https://tropica.com//en/plants/plantdetails/Utriculariagraminifolia(049BTC)/4480
https://tropica.com//en/plants/plantdetails/Vallisneriaamericana'Gigantea'(054)/4501
https://tropica.com//en/plants/plantdetails/Vallisneriaspiralis'Tiger'(055A)/4503
https://tropica.com//en/plants/plantdetails/Vesiculariaferriei'WeepingMoss'(003BPOR)/4398
https://tropica.com//en/plants/plantdetails/Vesiculariaferriei'WeepingMoss'(003BTC)/4399
https://tropica.com//en/plants/plantdetails/Vesiculariamontagnei'Christmas'(003AYWS)/4397
https://tropica.com//en/plants/plantdetails/Vesiculariamontagnei'ChristmasMoss'(003APOR)/4395
https://tropica.com//en/plants/plantdetails/Vesiculariamontagnei'ChristmasMoss'(003ATC)/4396
"""

# Sostituisci 'html_content' con il codice HTML della tabella
html_content = """
 <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Aegagropilalinnaei(000CST)/4385">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/000C ST/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Aegagropila linnaei</strong><br />
                                Moss<br />
                                (Item no. 000C ST)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Decorative algae balls</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Can be attached to pieces of wood or stone</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Also known as ‘Marimo’</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Aegagropilalinnaei(000DMP)/19534">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/000D MP/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Aegagropila linnaei</strong><br />
                                Moss<br />
                                (Item no. 000D MP)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Decorative algae balls</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Can be attached to pieces of wood or stone</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Also known as ‘Marimo’</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Alternantherareineckii&#39;Mini&#39;(023CTC)/4439">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/023C TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Alternanthera reineckii &#39;Mini&#39;</strong><br />
                                Stem<br />
                                (Item no. 023C TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Intensely pink red leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Compact and moderate growth rate</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Stays low if regularly trimmed</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Alternantherareineckii&#39;Pink&#39;(023XL)/4437">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/023 XL/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Alternanthera reineckii &#39;Pink&#39;</strong><br />
                                Stem<br />
                                (Item no. 023 XL)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>The leaf underside is pink</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Provides great contrast to green plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Also known as Alternanthera reineckii ‘Rosaefolia’</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Alternantherareineckii&#39;Pink&#39;(023)/4436">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/023/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Alternanthera reineckii &#39;Pink&#39;</strong><br />
                                Stem<br />
                                (Item no. 023)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>The leaf underside is pink</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Provides great contrast to green plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Also known as Alternanthera reineckii ‘Rosaefolia’</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Alternantherareineckii&#39;Rosanervig&#39;(023D)/4440">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/023D/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Alternanthera reineckii &#39;Rosanervig&#39;</strong><br />
                                Stem<br />
                                (Item no. 023D)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Vibrant pink leaves with light nerves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Compact and moderate growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Great eye-catcher among green plants</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Ammanniacrassicaulis(033B)/4449">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/033B/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Ammannia crassicaulis</strong><br />
                                Stem<br />
                                (Item no. 033B)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fast growing red stem plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Branches easily when it’s trimmed</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate by replanting the cut-offs</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarteri’CoinLeaf’(101F)/29447">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101F/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri ’Coin Leaf’ </strong><br />
                                Rhizomatous<br />
                                (Item no. 101F)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Nearly circular leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>A rich deep green color</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to grow plant </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbartericaladiifolia(101UPCS)/18816">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101U PCS/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri caladiifolia</strong><br />
                                Rhizomatous<br />
                                (Item no. 101U PCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Excellent plant for beginners </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Heart-shaped leaves, thrives at low light</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May be attached to pieces of rock and wood</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarteri&#39;MiniCoin&#39;(101BTC)/28816">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101B TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri &#39;Mini Coin&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 101B TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>New unique mini Anubias</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to grow and thrives in most aquariums</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Small, round and deep green leaves</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterinana(101TC)/18895">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101 TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri nana</strong><br />
                                Rhizomatous<br />
                                (Item no. 101 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the easiest plants for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives in shady places</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Ideal for planting on wood and rock pieces</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarteri&#39;Petite&#39;(101H)/4554">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101H/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri &#39;Petite&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 101H)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the smallest Anubias</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Ideal for planting on wood and rock pieces</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterisp.(101YWX)/4549">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101 YWX/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri sp.</strong><br />
                                Rhizomatous<br />
                                (Item no. 101 YWX)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Large mangrove wood with two self-attached Anubias</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterivar.barteri(101A)/4551">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri var. barteri</strong><br />
                                Rhizomatous<br />
                                (Item no. 101A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the easiest plants for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives in shady places</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Ideal for planting on wood and rock pieces</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterivar.caladiifolia(101UXL)/4557">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101U XL/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri var. caladiifolia</strong><br />
                                Rhizomatous<br />
                                (Item no. 101U XL)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Excellent plant for beginners </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Heart-shaped leaves, thrives at low light</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May be attached to pieces of rock and wood</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterivar.caladiifolia(101U)/4556">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101U/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri var. caladiifolia</strong><br />
                                Rhizomatous<br />
                                (Item no. 101U)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Excellent plant for beginners </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Heart-shaped leaves, thrives at low light</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May be attached to pieces of rock and wood</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterivar.&#39;Coffeifolia&#39;(101G)/4553">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101G/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri var. &#39;Coffeifolia&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 101G)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Ridged, deep green leaves and red shoots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Grows well on rock and wood pieces</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterivar.glabra(101C)/4552">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101C/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri var. glabra</strong><br />
                                Rhizomatous<br />
                                (Item no. 101C)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Tolerates very low light</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May be attached to pieces of rocks and wood</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterivar.nana(101PCS)/18806">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101 PCS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri var. nana</strong><br />
                                Rhizomatous<br />
                                (Item no. 101 PCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the easiest plants for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives in shady places</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Ideal for planting on wood and rock pieces</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterivar.nana(101YLS)/4546">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101 YLS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri var. nana</strong><br />
                                Rhizomatous<br />
                                (Item no. 101 YLS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Lava rock with self-attached Anubias</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterivar.nana(101YWS)/4548">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101 YWS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri var. nana</strong><br />
                                Rhizomatous<br />
                                (Item no. 101 YWS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Mangrove wood with self-attached Anubias</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterivar.nana(101ZWS)/4550">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101 ZWS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri var. nana</strong><br />
                                Rhizomatous<br />
                                (Item no. 101 ZWS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Mangrove wood with suction cup and self-attached Anubias</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the glass of the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterivar.nana(101)/4545">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri var. nana</strong><br />
                                Rhizomatous<br />
                                (Item no. 101)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the easiest plants for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives in shady places</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Ideal for planting on wood and rock pieces</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterivar.nana(510YCS)/28184">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/510 YCS/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri var. nana</strong><br />
                                Rhizomatous<br />
                                (Item no. 510 YCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Perfect hiding spot for livestock</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Sturdy roots keep the plant in place</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>A pleasant eye catcher from the start</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterivar.nana’Kirin’(101K)/29448">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101K/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri var. nana ’Kirin’ </strong><br />
                                Rhizomatous<br />
                                (Item no. 101K)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Leaves with strongly wavy edges</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives in low-light conditions</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Inspired by an Asian dragon</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterivar.nana’Pinto’(101E)/29446">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101E/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri var. nana ’Pinto’ </strong><br />
                                Rhizomatous<br />
                                (Item no. 101E)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Leaves showcase captivating patterns of white, light and dark green</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Slow growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>To be attached to rocks or wood in the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasbarterivar.nana&#39;Large&#39;(101L)/19785">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101L/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias barteri var. nana &#39;Large&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 101L)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the easiest plants for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives in shady places</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Ideal for planting on wood and rock pieces</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Anubiasgracilis(101D)/17819">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/101D/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Anubias gracilis</strong><br />
                                Rhizomatous<br />
                                (Item no. 101D)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful triangular leaves on long stems</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Tolerates low light conditions</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Grows well on wood and rock pieces</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Aponogetonboivinianus(088KN)/4534">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/088 KN/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Aponogeton boivinianus</strong><br />
                                Bulb/onion<br />
                                (Item no. 088 KN)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Outstanding and very large solitary plant </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Bulb plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Requires a dormant period</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Aponogetonlongiplumulosus(089DKN)/4536">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/089D KN/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Aponogeton longiplumulosus</strong><br />
                                Bulb/onion<br />
                                (Item no. 089D KN)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful and distinctive solitary plant </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Bulb plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Requires a dormant period</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Aponogetonmadagascariensis(089KN)/4535">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/089 KN/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Aponogeton madagascariensis</strong><br />
                                Bulb/onion<br />
                                (Item no. 089 KN)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Outstanding and unique solitary plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Bulb plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Also called Madagascar Lace Plant</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Aponogetonulvaceus(086KN)/4533">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/086 KN/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Aponogeton ulvaceus</strong><br />
                                Bulb/onion<br />
                                (Item no. 086 KN)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very big, magnificent solitary plant </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Bulb plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May require a dormant period</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bacopaaustralis(043A)/4466">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/043A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bacopa australis</strong><br />
                                Stem<br />
                                (Item no. 043A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Bright green stem plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>When the conditions are optimal, the growth is creeping</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Originates from Brazil, not Australia</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bacopacaroliniana(043BDT)/4465">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/043 BDT/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bacopa caroliniana</strong><br />
                                Stem<br />
                                (Item no. 043 BDT)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding beginner’s plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Stem plant of moderate growth </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Cut-off shoots will easily form new plants</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bacopacaroliniana(043MP)/18811">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/043 MP/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bacopa caroliniana</strong><br />
                                Stem<br />
                                (Item no. 043 MP)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding beginner’s plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Stem plant of moderate growth </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Cut-off shoots will easily form new plants</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bacopacaroliniana(043TC)/18752">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/043 TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bacopa caroliniana</strong><br />
                                Stem<br />
                                (Item no. 043 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding beginner’s plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Stem plant of moderate growth </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Cut-off shoots will easily form new plants</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bacopacaroliniana(043)/4464">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/043/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bacopa caroliniana</strong><br />
                                Stem<br />
                                (Item no. 043)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding beginner’s plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Stem plant of moderate growth </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Cut-off shoots will easily form new plants</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bacopamonnieri&#39;Compact&#39;(044APCS)/18800">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/044A PCS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bacopa monnieri &#39;Compact&#39;</strong><br />
                                Stem<br />
                                (Item no. 044A PCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Low and compact stem plan</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Cutting top shoots will increase side shoots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Endures bad light conditions but growth will become more vertical</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bacopamonnieri&#39;Compact&#39;(044A)/4467">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/044A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bacopa monnieri &#39;Compact&#39;</strong><br />
                                Stem<br />
                                (Item no. 044A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Low and compact stem plan</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Cutting top shoots will increase side shoots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Endures bad light conditions but growth will become more vertical</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Blyxajaponica(057TC)/22542">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/057 TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Blyxa japonica</strong><br />
                                Rosulate<br />
                                (Item no. 057 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful reddish color under the right light conditions </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Only grows submerse </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Best employed in aquariums with moderate to high lighting and CO2</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bolbitisheudelotii(006XL)/18376">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/006 XL/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bolbitis heudelotii</strong><br />
                                Rhizomatous<br />
                                (Item no. 006 XL)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fern with translucent, dark green and lobed leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very decorative when attached to pieces of rock or wood</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Does not thrive in very chalky water</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bolbitisheudelotii(006YWS)/4407">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/006 YWS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bolbitis heudelotii</strong><br />
                                Rhizomatous<br />
                                (Item no. 006 YWS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Mangrove wood with self-attached Bolbitis</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bolbitisheudelotii(006)/4406">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/006/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bolbitis heudelotii</strong><br />
                                Rhizomatous<br />
                                (Item no. 006)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fern with translucent, dark green and lobed leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very decorative when attached to pieces of rock or wood</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Does not thrive in very chalky water</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bucephalandra&#39;Kedagang&#39;(139BTC)/22544">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/139B TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bucephalandra &#39;Kedagang&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 139B TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to attach to a hardscape of choice</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Unique underwater colour appears </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Resilient and adaptable to different water parameters </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bucephalandra&#39;Kedagang&#39;(139B)/22543">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/139B/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bucephalandra &#39;Kedagang&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 139B)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to attach to a hardscape of choice</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Unique underwater colouappearrs </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Resilient and adaptable to different water parameters </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bucephalandrapygmaea&#39;BukitKelam&#39;(139TC)/28393">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/139 TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bucephalandra pygmaea &#39;Bukit Kelam&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 139 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Branches willingly without trimming</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Ideal for growing on rocks and wood pieces</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bucephalandrapygmaea&#39;BukitKelam&#39;(139)/18757">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/139/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bucephalandra pygmaea &#39;Bukit Kelam&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 139)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Branches willingly without trimming</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Ideal for growing on rocks and wood pieces</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bucephalandrapygmaea&#39;WavyGreen&#39;(139YLS)/18758">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/139 YLS/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bucephalandra pygmaea &#39;Wavy Green&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 139 YLS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Lava rock with self-attached Bucephalandra</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer of the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bucephalandrasp.&#39;NeedleLeaf&#39;(139CTC)/29517">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/139C TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bucephalandra sp. &#39;Needle Leaf&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 139C TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>A very easy plant to grow</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Immersed leaves are green showing numerous tiny, white dots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Youngest parts of the rhizome display a nice, red colour</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Bucephalandrasp.&#39;Red&#39;(139A)/19682">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/139A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Bucephalandra sp. &#39;Red&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 139A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Branches willingly without trimming</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Ideal for growing on rocks and wood pieces</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cabombaaquatica(015BDT)/4431">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/015 BDT/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cabomba aquatica</strong><br />
                                Stem<br />
                                (Item no. 015 BDT)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and decorative stem plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Elegant, feathery leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Suitable as auxiliary plant in newly started aquariums</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cardaminelyrata(024)/4441">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/024/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cardamine lyrata</strong><br />
                                Stem<br />
                                (Item no. 024)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Grows vertically which makes it perfect for backgrounds</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Bright, pale green colour that will enhance the shades of surrounding, red plants </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Undemanding, but develops orange shoots at very intense light</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Ceratophyllumdemersum(021APOR)/4434">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/021A POR/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Ceratophyllum demersum</strong><br />
                                Stem<br />
                                (Item no. 021A POR)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding floating plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Offers excellent hiding for fish spawn and fry</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Helps prevent algae growth</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Ceratopteristhalictroides(005A)/4405">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/005A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Ceratopteris thalictroides</strong><br />
                                Rosulate<br />
                                (Item no. 005A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Finely branched, bright green leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Grows fast, which helps preventing algae growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Also suitable as floating plant</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Crinumcalamistratum(094A)/4541">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/094A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Crinum calamistratum</strong><br />
                                Bulb/onion<br />
                                (Item no. 094A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Outstanding and beautiful solitary plant </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Bulb plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Is normally not eaten by herbivorous fish</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Crinumthaianum(093)/4537">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/093/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Crinum thaianum</strong><br />
                                Bulb/onion<br />
                                (Item no. 093)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very large and distinctive solitary plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Most suited for big aquariums</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Is normally not eaten by herbivorous fish</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocorynealbida&#39;Brown&#39;(126B)/18194">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/126B/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne albida &#39;Brown&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 126B)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Narrow, maroon leaves with black markings</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very low growing Cryptocoryne</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocorynebeckettii&#39;Petchii&#39;(108APCS)/18807">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/108A PCS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne beckettii &#39;Petchii&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 108A PCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the very easiest Cryptocorynes</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Great plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Remains relatively low in the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocorynebeckettii&#39;Petchii&#39;(108AYLS)/4561">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/108A YLS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne beckettii &#39;Petchii&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 108A YLS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Lava rock with self-attached Cryptocorynes</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer of the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocorynebeckettii&#39;Petchii&#39;(108A)/4560">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/108A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne beckettii &#39;Petchii&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 108A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the very easiest Cryptocorynes</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Great plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Remains relatively low in the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocorynecrispatula(125TC)/18756">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/125 TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne crispatula</strong><br />
                                Rosulate<br />
                                (Item no. 125 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Long, narrow and hammered leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the taller Cryptocorynes</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Needs good light and fertilisers to thrive</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocorynecrispatula(125)/4567">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/125/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne crispatula</strong><br />
                                Rosulate<br />
                                (Item no. 125)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Long, narrow and hammered leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the taller Cryptocorynes</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Needs good light and fertilisers to thrive</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocorynenurii(126TC)/29518">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/126 TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne nurii </strong><br />
                                Rosulate<br />
                                (Item no. 126 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Intensity of colour and patterns is dependant on light and nutrition</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Is easy to grow</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Popular under the name &#39;Rose Maiden&#39;</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocoryneparva(106TC)/18755">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/106 TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne parva</strong><br />
                                Rosulate<br />
                                (Item no. 106 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Smallest Cryptocoryne - only 3-6cm tall</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Slow growth </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Can develop into a carpet</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocoryneparva(106)/4558">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/106/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne parva</strong><br />
                                Rosulate<br />
                                (Item no. 106)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the smallest Cryptocorynes</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Over time, it will form a beautiful carpet </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Requires good light and nutrient conditions to develop well</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocoryneundulata&#39;BroadLeaf&#39;(110A)/4566">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/110A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne undulata &#39;Broad Leaf&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 110A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Robust plant suited for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautifully flecked leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the taller Cryptocorynes</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocoryneundulata&#39;BroadLeaf&#39;(110BTC)/19225">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/110B TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne undulata &#39;Broad Leaf&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 110B TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and sure plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Leaves become reddish when conditions are good</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Medium tall Cryptocoryne</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocoryneusteriana(120)/18405">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/120/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne usteriana</strong><br />
                                Rosulate<br />
                                (Item no. 120)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the tallest Cryptocorynes</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautifully hammered leaves with red underside</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Tolerates rather alkaline water</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocorynewendtii&#39;Green&#39;(109TC)/19226">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/109 TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne wendtii &#39;Green&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 109 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Green and low maintenance Cryptocoryne</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Great plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives in shady places in the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocorynewendtii&#39;Green&#39;(109)/4562">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/109/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne wendtii &#39;Green&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 109)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Green and low maintenance Cryptocoryne</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Great plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives in shady places in the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocorynewendtii&#39;MiOya&#39;(109DTC)/19540">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/109D TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne wendtii &#39;Mi Oya&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 109D TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Red-brown, slightly hammered leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Can grow at high temperatures</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>15-30 cm wide rosettes</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocorynewendtii&#39;Tropica&#39;(109EXL)/4565">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/109E XL/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne wendtii &#39;Tropica&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 109E XL)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and hardy plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Dark, ruffled leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Tolerates shade from other plants</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocorynewendtii&#39;Tropica&#39;(109E)/4564">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/109E/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne wendtii &#39;Tropica&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 109E)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and hardy plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Dark, ruffled leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Tolerates shade from other plants</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocorynexwillisii(107PCS)/19618">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/107 PCS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne x willisii</strong><br />
                                Rosulate<br />
                                (Item no. 107 PCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May need some time to start growing</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Used to be called Cryptocoryne nevillii</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cryptocorynexwillisii(107)/4559">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/107/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cryptocoryne x willisii</strong><br />
                                Rosulate<br />
                                (Item no. 107)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May need some time to start growing</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Used to be called Cryptocoryne nevillii</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Cyperushelferi(133A)/4574">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/133A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Cyperus helferi</strong><br />
                                Rosulate<br />
                                (Item no. 133A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Tall, light green grass</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Offers great contrast to other other leaf forms</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Sways gently in the water stream</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorus&#39;Aquartica&#39;(074F)/4526">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/074F/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus &#39;Aquartica&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 074F)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful pale green, solitary plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Rounded leaves and low growth in the aquarium</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Suitable for smaller aquariums</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodoruscordifolius&#39;Fluitans&#39;(073D)/4519">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/073D/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus cordifolius &#39;Fluitans&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 073D)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Wavy, pale green leaves in the tank</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>The leaves usually stay under the water surface</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorusgrisebachii&#39;Bleherae&#39;(071BDT)/4513">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/071 BDT/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus grisebachii &#39;Bleherae&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 071 BDT)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very easy and undemanding beginner’s plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives at rather low light intensity</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Previously named Echinodorus ’paniculatus’</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorusgrisebachii&#39;Bleherae&#39;(071XL)/21211">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/071 XL/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus grisebachii &#39;Bleherae&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 071 XL)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very easy and undemanding beginner’s plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives at rather low light intensity</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Previously named Echinodorus ’paniculatus’</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorusgrisebachii&#39;Bleherae&#39;(071)/4512">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/071/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus grisebachii &#39;Bleherae&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 071)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very easy and undemanding beginner’s plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives at rather low light intensity</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Previously named Echinodorus ’paniculatus’</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorus&#39;Ozelot&#39;(073FXL)/4521">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/073F XL/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus &#39;Ozelot&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 073F XL)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very beautiful as solitary plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Large, maroon leaves with decorative, dark spots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy plant for beginners</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorus&#39;Ozelot&#39;(073F)/4520">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/073F/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus &#39;Ozelot&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 073F)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very beautiful as solitary plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Large, maroon leaves with decorative, dark spots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy plant for beginners</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorus&#39;OzelotGreen&#39;(073G)/4522">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/073G/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus &#39;Ozelot Green&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 073G)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful solitary plant of contrasting colours</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Pale green, wavy and spotted leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodoruspalifolius(076XL)/4528">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/076 XL/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus palifolius</strong><br />
                                Rosulate<br />
                                (Item no. 076 XL)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Upright growing solitary plant for larger aquariums</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>The leaves will often pass the surface of the water</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Particularly suitable for open aquariums</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodoruspalifolius(076)/4527">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/076/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus palifolius</strong><br />
                                Rosulate<br />
                                (Item no. 076)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Upright growing solitary plant for larger aquariums</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>The leaves will often pass the surface of the water</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Particularly suitable for open aquariums</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorus&#39;RedDiamond&#39;(074D)/4525">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/074D/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus &#39;Red Diamond&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 074D)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful, red solitary plant </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the smallest red Echinodorus</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy plant for beginners</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorus&#39;Reni&#39;(072DPCS)/18818">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/072D PCS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus &#39;Reni&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 072D PCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful red and green solitary plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the smallest Echinodorus</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy plant for beginners, well suited for smaller aquariums</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorus&#39;Reni&#39;(072DTC)/18754">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/072D TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus &#39;Reni&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 072D TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful red and green solitary plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the smallest Echinodorus</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy plant for beginners, well suited for smaller aquariums</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorus&#39;Reni&#39;(072D)/4518">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/072D/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus &#39;Reni&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 072D)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful red and green solitary plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the smallest Echinodorus</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy plant for beginners, well suited for smaller aquariums</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorus&#39;Ros&#233;&#39;(072BXL)/4517">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/072B XL/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus &#39;Ros&#233;&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 072B XL)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful pink and green solitary plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May overshadow smaller plants</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorus&#39;Ros&#233;&#39;(072B)/4516">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/072B/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus &#39;Ros&#233;&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 072B)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful pink and green solitary plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May overshadow smaller plants</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorusxbarthii(072AXL)/4515">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/072A XL/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus x barthii</strong><br />
                                Rosulate<br />
                                (Item no. 072A XL)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful red and green solitary plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Good light and nutrient conditions will enhance the coloration</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Previously named &quot;Double Red&quot;</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Echinodorusxbarthii(072A)/4514">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/072A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Echinodorus x barthii</strong><br />
                                Rosulate<br />
                                (Item no. 072A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful red and green solitary plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Good light and nutrient conditions will enhance the coloration</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Previously named &quot;Double Red&quot;</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Egeriadensa(058BDT)/4506">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/058 BDT/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Egeria densa</strong><br />
                                Stem<br />
                                (Item no. 058 BDT)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the easiest stem plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Good auxiliary plant, when starting an aquarium</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fast-growing and helps prevent algae propagation</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Elatinehydropiper(141TC)/18759">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/141 TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Elatine hydropiper</strong><br />
                                Carpeting<br />
                                (Item no. 141 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the smallest aquarium plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Rather slow-growing carpeting plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Its colour stunningly compliments rocks and wood pieces </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Eleocharisacicularis(133TC)/28401">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/133 TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Eleocharis acicularis</strong><br />
                                Stolon<br />
                                (Item no. 133 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Carpeting plant for foreground </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May be cut down to the preferred height</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Eleocharismontevidensis(132D)/4573">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/132D/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Eleocharis montevidensis</strong><br />
                                Stolon<br />
                                (Item no. 132D)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Pretty, tall grass-like leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May help create great perspective and depth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Its growth will continue to allow looking through the leaves</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Eleocharisparvula(132C)/4572">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/132C/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Eleocharis parvula</strong><br />
                                Carpeting<br />
                                (Item no. 132C)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very safe and easy carpeting plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Quickly grows to a dense lawn </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Requires frequent trimming to stay low</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Eleocharispusilla&#39;Mini&#39;(132BTC)/4571">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/132B TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Eleocharis pusilla &#39;Mini&#39;</strong><br />
                                Carpeting<br />
                                (Item no. 132B TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the most popular foreground plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Quick and safe carpeting growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Ideal for nano tanks and for planting between rocks</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Eriocauloncinereum(091TC)/19547">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/091 TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Eriocaulon cinereum</strong><br />
                                Rosulate<br />
                                (Item no. 091 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very characteristic look, resembling a pin cushion</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Flowers willingly in the aquarium after planting</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Does not thrive in hard water</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Fissidensfontanus(002F)/4390">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/002F/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Fissidens fontanus</strong><br />
                                Moss<br />
                                (Item no. 002F)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Featherlike, dark green moss </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>To be attached to rocks and wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Will attach itself to rocks and wood after some time</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Glossostigmaelatinoides(045ATC)/4470">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/045A TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Glossostigma elatinoides</strong><br />
                                Carpeting<br />
                                (Item no. 045A TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Popular, fast-growing and very pretty carpeting plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Requires intense light and CO2 addition to thrive</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Frequent trimming is necessary due to the fast growth </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Gratiolaviscidula(042TC)/18390">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/042 TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Gratiola viscidula</strong><br />
                                Stem<br />
                                (Item no. 042 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Distinct and easily recognizable</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Looks thorny, but doesn’t sting</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very low and compact growth</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Helanthiumbolivianum&#39;Quadricostatus&#39;(068TC)/18896">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/068 TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Helanthium bolivianum &#39;Quadricostatus&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 068 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Small, light green rosette plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives at low light conditions</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Previously named Echinodorus quadricostatus</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Helanthiumbolivianum&#39;Quadricostatus&#39;(068)/4511">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/068/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Helanthium bolivianum &#39;Quadricostatus&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 068)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Small, light green rosette plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives at low light conditions</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Previously named Echinodorus quadricostatus</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Helanthiumtenellum&#39;Green&#39;(067ATC)/4757">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/067A TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Helanthium tenellum &#39;Green&#39;</strong><br />
                                Carpeting<br />
                                (Item no. 067A TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding foreground plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Vivid, bright green colour</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Spreads readily with runners</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hemianthusmicranthemoides(048ATC)/22879">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/048A TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hemianthus micranthemoides</strong><br />
                                Carpeting<br />
                                (Item no. 048A TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Versatile plant, can be placed anywhere in the aquarium</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fast grower in the right conditions </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Unique leave-shape</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Heterantherazosterifolia(096TC)/4544">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/096 TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Heteranthera zosterifolia</strong><br />
                                Stem<br />
                                (Item no. 096 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the easiest plants for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very suited when starting an aquarium</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate by planting the cuttings</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hottoniapalustris(027TC)/28508">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/027 TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hottonia palustris</strong><br />
                                Stem<br />
                                (Item no. 027 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding beginner’s plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Lobed leaves of intense, bright green colour</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Helps create an excellent transition between low and tall plants</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hottoniapalustris(027)/4443">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/027/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hottonia palustris</strong><br />
                                Stem<br />
                                (Item no. 027)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding beginner’s plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Lobed leaves of intense, bright green colour</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Helps create an excellent transition between low and tall plants</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hydrocotyletripartita(039BTC)/18751">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/039B TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hydrocotyle tripartita</strong><br />
                                Stem<br />
                                (Item no. 039B TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fast, carpeting growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Vivid bright green colour</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Press it with your palm to obtain better carpeting growth</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hydrocotyletripartita(039B)/4458">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/039B/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hydrocotyle tripartita</strong><br />
                                Stem<br />
                                (Item no. 039B)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fast, carpeting growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Vivid bright green colour</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Press it with your palm to obtain better carpeting growth</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hydrocotyleverticillata(039)/4457">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/039/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hydrocotyle verticillata</strong><br />
                                Stem<br />
                                (Item no. 039)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful carpeting plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Requires high light intensity to thrive at its best</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Can be used as floating plant</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilacorymbosa(053BDT)/4490">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053 BDT/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila corymbosa</strong><br />
                                Stem<br />
                                (Item no. 053 BDT)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Large, wide pale green leaves in the aquarium</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate by planting cut-off shoots</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilacorymbosa&#39;Compact&#39;(052D)/18774">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/052D/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila corymbosa &#39;Compact&#39;</strong><br />
                                Stem<br />
                                (Item no. 052D)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Compact variant of Hygrophila corymbosa</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Pale, green leaves with silvery-white underside in the aquarium</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Potentially grows excrescences, which should be removed</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilacorymbosa&#39;Siamensis53B&#39;(053BMP)/18813">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053B MP/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila corymbosa &#39;Siamensis 53B&#39;</strong><br />
                                Stem<br />
                                (Item no. 053B MP)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very bushy growth, thanks to its multiple side shoots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate by planting cut-off shoots</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilacorymbosa&#39;Siamensis53B&#39;(053BPCS)/18803">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053B PCS/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila corymbosa &#39;Siamensis 53B&#39;</strong><br />
                                Stem<br />
                                (Item no. 053B PCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very bushy growth, thanks to its multiple side shoots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate by planting cut-off shoots</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilacorymbosa&#39;Siamensis53B&#39;(053B)/4493">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053B/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila corymbosa &#39;Siamensis 53B&#39;</strong><br />
                                Stem<br />
                                (Item no. 053B)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very bushy growth, thanks to its multiple side shoots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate by planting cut-off shoots</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilacorymbosa&#39;Stricta&#39;(053AXL)/4492">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053A XL/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila corymbosa &#39;Stricta&#39;</strong><br />
                                Stem<br />
                                (Item no. 053A XL)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fast-growing and great auxiliary plant when starting a tank</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate by planting cut-off shoots</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilacorymbosa&#39;Stricta&#39;(053A)/4491">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila corymbosa &#39;Stricta&#39;</strong><br />
                                Stem<br />
                                (Item no. 053A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy not demanding beginner plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fast growing and good for starting the aquarium</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate by cuttings</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilacostata(052A)/4489">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/052A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila costata</strong><br />
                                Stem<br />
                                (Item no. 052A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Forms long, narrow leaves in the aquarium</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate by planting cut-off shoots</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophiladifformis(051BDT)/4485">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/051 BDT/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila difformis</strong><br />
                                Stem<br />
                                (Item no. 051 BDT)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the easiest plants for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Great as auxiliary plant when starting a tank</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Pretty, light green, lobed leaves</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilalancea&#39;Araguaia&#39;(051BTC)/4758">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/051B TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila lancea &#39;Araguaia&#39;</strong><br />
                                Stem<br />
                                (Item no. 051B TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautifully coloured stem plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Low and compact growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Moderate growth rate</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilapinnatifida(051ATC)/19228">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/051A TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila pinnatifida</strong><br />
                                Stem<br />
                                (Item no. 051A TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very distinctive leaf shape and colour</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May be planted on wood and rocks</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Remove top shoots to keep it low and compact</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilapinnatifida(051A)/4486">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/051A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila pinnatifida</strong><br />
                                Stem<br />
                                (Item no. 051A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very distinctive leaf form and colour</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May be planted on wood and rocks</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Remove top shoots to keep it low and compact</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilapinnatifida(509YCS)/28279">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/509 YCS/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila pinnatifida</strong><br />
                                Stem<br />
                                (Item no. 509 YCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Stunning colors under the right conditions </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Instant mini aquascape</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Ideal hiding spot for livestock</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilapinnatifidaandmoss(051AYWS)/4487">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/051A YWS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila pinnatifida and moss</strong><br />
                                Stem<br />
                                (Item no. 051A YWS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Mangrove wood with moss and self-attached Hygrophila pinnatifida</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilapolysperma(050)/4483">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/050/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila polysperma</strong><br />
                                Stem<br />
                                (Item no. 050)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the easiest plants for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Great auxiliary plant when starting a tank</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate by planting cut-off shoots</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Hygrophilapolysperma&#39;Rosanervig&#39;(050B)/4484">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/050B/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Hygrophila polysperma &#39;Rosanervig&#39;</strong><br />
                                Stem<br />
                                (Item no. 050B)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Requires high light intensity to develop intense, pink colouring</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Green shoots should be removed</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Juncusrepens			(133FTC)/28107">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/133F TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Juncus repens			</strong><br />
                                Stem<br />
                                (Item no. 133F TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to grow underwater</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Stunning green color under moderate light</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Reddish-brown hue under a strong light </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Lagenandrameeboldii&#39;Red&#39;(103)/4759">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/103/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Lagenandra meeboldii &#39;Red&#39;</strong><br />
                                Rosulate<br />
                                (Item no. 103)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful colourings on the leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Good light conditions will enhance the development of colours</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Leptodictyumriparium(003ETC)/28671">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/003E TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Leptodictyum riparium</strong><br />
                                Moss<br />
                                (Item no. 003E TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>An easy category plant that can grow in most aquariums. </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate by simply planting a &quot;tot&quot; somewhere else</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Grows easily on rocks and roots</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Lilaeopsisbrasiliensis(040PCS)/18808">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/040 PCS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Lilaeopsis brasiliensis</strong><br />
                                Stolon<br />
                                (Item no. 040 PCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding carpeting plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Propagates easily with stolons</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives also at low light</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Lilaeopsisbrasiliensis(040TC)/4460">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/040 TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Lilaeopsis brasiliensis</strong><br />
                                Stolon<br />
                                (Item no. 040 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding carpeting plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Propagates easily with stolons</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives also at low light</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Lilaeopsisbrasiliensis(040)/4459">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/040/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Lilaeopsis brasiliensis</strong><br />
                                Stolon<br />
                                (Item no. 040)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding carpeting plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Propagates easily with stolons</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives also at low light</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Limnobiumlaevigatum(063TC)/4761">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/063 TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Limnobium laevigatum</strong><br />
                                Floating plant<br />
                                (Item no. 063 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very easy and fast-growing surface plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Helps prevent algae propagation in the tank</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Indicates the presence of nutrients in the water</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Limnophilaaquatica(046)/4471">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/046/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Limnophila aquatica</strong><br />
                                Stem<br />
                                (Item no. 046)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the most beautiful green stem plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and fast-growing</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Great auxiliary plant when creating a new tank</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Limnophilahippuridoides(047C)/4474">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/047C/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Limnophila hippuridoides</strong><br />
                                Stem<br />
                                (Item no. 047C)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy stem plant with purple leaf undersides</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives at various light intensities</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Needs added CO2 and strong light to develop intense purple leaf colour</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Limnophilasessiliflora(047MP)/18812">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/047 MP/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Limnophila sessiliflora</strong><br />
                                Stem<br />
                                (Item no. 047 MP)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the easiest aquarium plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful, fast growing stems</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Great auxiliary plant when starting a new tank</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Limnophilasessiliflora(047PCS)/18801">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/047 PCS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Limnophila sessiliflora</strong><br />
                                Stem<br />
                                (Item no. 047 PCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the easiest aquarium plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful, fast growing stems</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Great auxiliary plant when starting a new tank</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Limnophilasessiliflora(047)/4472">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/047/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Limnophila sessiliflora</strong><br />
                                Stem<br />
                                (Item no. 047)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the easiest aquarium plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful, fast growing stems</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Great auxiliary plant when starting a new tank</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Linderniarotundifolia(045)/4468">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/045/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Lindernia rotundifolia</strong><br />
                                Stem<br />
                                (Item no. 045)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful, marbled leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Dense and lush growth</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Littorellauniflora(081TC)/18269">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/081 TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Littorella uniflora</strong><br />
                                Stolon<br />
                                (Item no. 081 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Distinctive, thick leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Foreground plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Tolerates low light intensity</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Lobeliacardinalis(053CMP)/18840">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053C MP/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Lobelia cardinalis</strong><br />
                                Stem<br />
                                (Item no. 053C MP)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and hardy plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Leaves become light green in the aquarium</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Suitable for the garden pond</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Lobeliacardinalis(053CPCS)/21134">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053C PCS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Lobelia cardinalis</strong><br />
                                Stem<br />
                                (Item no. 053C PCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and hardy plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Leaves become light green in the aquarium</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Suitable for the garden pond</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Lobeliacardinalis(053C)/4494">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053C/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Lobelia cardinalis</strong><br />
                                Stem<br />
                                (Item no. 053C)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and hardy plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Leaves become light green in the aquarium</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Suitable for the garden pond</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Lobeliacardinalis&#39;Mini&#39;(143TC)/28647">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/143 TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Lobelia cardinalis &#39;Mini&#39;</strong><br />
                                Stem<br />
                                (Item no. 143 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful green colour with compact growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate in the aquarium - and a safe choice for most aquarists.</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives in many aquariums but more CO2, light and fertilizer will increase the plant&#39;s growth, compactness, and colour intensity.</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Ludwigiaglandulosa(035A)/4452">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/035A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Ludwigia glandulosa</strong><br />
                                Stem<br />
                                (Item no. 035A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Magnificent, intense red stem plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fairly slow growing</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Previously named Ludwigia perennis</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Ludwigiapalustris&#39;SuperRed&#39;(035B)/4453">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/035B/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Ludwigia palustris &#39;Super Red&#39;</strong><br />
                                Stem<br />
                                (Item no. 035B)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the easiest, red stem plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Branches willingly</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Cut-off shoots will form new plants </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Ludwigiarepens&#39;Rubin&#39;(033D)/4450">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/033D/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Ludwigia repens &#39;Rubin&#39;</strong><br />
                                Stem<br />
                                (Item no. 033D)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Offers a beautiful contrast to green plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Red coloration will intensify at high light levels</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Marsileahirsuta(010TC)/4428">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/010 TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Marsilea hirsuta</strong><br />
                                Carpeting<br />
                                (Item no. 010 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and secure carpeting plant </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Does not require high light intensity</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Its many roots anchors it well in the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Marsileaminuta(010BTC)/4762">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/010B TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Marsilea minuta</strong><br />
                                Carpeting<br />
                                (Item no. 010B TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the smallest carpeting plants for aquariums</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Bright, pale green colour</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Tolerates high temperatures</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Mayacafluviatilis(140BDT)/19792">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/140 BDT/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Mayaca fluviatilis</strong><br />
                                Stem<br />
                                (Item no. 140 BDT)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Exceptional, light and delicate stem plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Needs good conditions to thrive well</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate by planting the cut-off shoots</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Micranthemumcallitrichoides&#180;Cuba&#180;(048B)/4477">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/048B/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Micranthemum callitrichoides &#180;Cuba&#180;</strong><br />
                                Carpeting<br />
                                (Item no. 048B)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the most popular carpeting plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Quickly forms a dense, bright green carpet</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Need regular trims to stay healthy</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Micranthemumcallitrichoides&#39;Cuba&#39;(048BTC)/4478">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/048B TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Micranthemum callitrichoides &#39;Cuba&#39;</strong><br />
                                Carpeting<br />
                                (Item no. 048B TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the most popular carpeting plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Quickly forms a dense, bright green carpet</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Need regular trims to stay healthy</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Micranthemumglomeratum(048A)/4476">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/048A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Micranthemum glomeratum</strong><br />
                                Carpeting<br />
                                (Item no. 048A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Elegant, small-leaved stem plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Forms a bright green carpet at high light intensity</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May be used in terrariums</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Micranthemumtweediei&#39;MonteCarlo&#39;(025TC)/4442">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/025 TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Micranthemum tweediei &#39;Monte Carlo&#39;</strong><br />
                                Carpeting<br />
                                (Item no. 025 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful light green and carpeting</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Much easier to grow than Micranthemum callitrichoides &#180;Cuba&#180;</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Requires regular trims to stay low and compact</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Micranthemumtweediei&#39;MonteCarlo&#39;(025)/22880">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/025/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Micranthemum tweediei &#39;Monte Carlo&#39;</strong><br />
                                Carpeting<br />
                                (Item no. 025)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful light green and carpeting</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Much easier to grow than Micranthemum callitrichoides &#180;Cuba&#180;</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Requires regular trims to stay low and compact</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Micranthemumumbrosum(048ST)/19793">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/048 ST/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Micranthemum umbrosum</strong><br />
                                Stem<br />
                                (Item no. 048 ST)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Elegant, small-leaved stem plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Vivid, bright green colour</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Well suited for small aquariums</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Micranthemumumbrosum(048)/4475">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/048/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Micranthemum umbrosum</strong><br />
                                Stem<br />
                                (Item no. 048)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Elegant, small-leaved stem plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Vivid, bright green colour</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Well suited for small aquariums</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorum-Anubias&#39;Duet&#39;(008NYWX)/4427">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008N YWX/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum - Anubias &#39;Duet&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 008N YWX)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Large mangrove wood with self-attached Microsorum and Anubias</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus(008XL)/4409">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008 XL/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus</strong><br />
                                Rhizomatous<br />
                                (Item no. 008 XL)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very decorative when attached to rocks and wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Known also as Java fern</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus(008YLS)/4410">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008 YLS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus</strong><br />
                                Rhizomatous<br />
                                (Item no. 008 YLS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Lava rock with self-attached Microsorum</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer of the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus(008YWS)/4412">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008 YWS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus</strong><br />
                                Rhizomatous<br />
                                (Item no. 008 YWS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Mangrove wood with self-attached Microsorum</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus(008YWX)/4413">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008 YWX/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus</strong><br />
                                Rhizomatous<br />
                                (Item no. 008 YWX)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Mangrove wood with two self-attached Microsorums</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus(008)/4408">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus</strong><br />
                                Rhizomatous<br />
                                (Item no. 008)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very decorative when attached to rocks and wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Known also as Java fern</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus&#39;Narrow&#39;(008APCS)/18821">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008A PCS/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus &#39;Narrow&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 008A PCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very decorative when fastened to rocks or wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>The leaves are smaller and narrower than those of the classic Java fern</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus&#39;Narrow&#39;(008AYWS)/4415">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008A YWS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus &#39;Narrow&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 008A YWS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Mangrove wood with self-attached Microsorum</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus&#39;Narrow&#39;(008AZWS)/4417">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008A ZWS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus &#39;Narrow&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 008A ZWS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Mangrove wood with suction cup and self-attached Microsorum</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the glass of the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus&#39;Narrow&#39;(008A)/4414">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus &#39;Narrow&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 008A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very decorative when fastened to rocks or wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>The leaves are smaller and narrower than those of the classic Java fern</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus&#39;Trident&#39;(008GYWS)/4425">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008G YWS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus &#39;Trident&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 008G YWS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Mangrove wood with self-attached Microsorum</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus&#39;Trident&#39;(008GZWM)/4426">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008G ZWM/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus &#39;Trident&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 008G ZWM)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Mangrove wood with suction cup and self-attached Microsorum</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the glass of the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus&#39;Trident&#39;(008GZWS)/19275">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008G ZWS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus &#39;Trident&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 008G ZWS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Mangrove wood with suction cup and self-attached Microsorum</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the glass of the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus&#39;Trident&#39;(008G)/4424">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008G/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus &#39;Trident&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 008G)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners, often with lobed leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very decorative when fastened to rocks or wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Grows more horizontally than the other Microsorum</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus&#39;Windel&#248;v&#39;(008BYWS)/4420">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008B YWS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus &#39;Windel&#248;v&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 008B YWS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Mangrove wood with self-attached Microsorum</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus&#39;Windel&#248;v&#39;(008BYWX)/4421">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008B YWX/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus &#39;Windel&#248;v&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 008B YWX)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Large mangrove wood with two self-attached Microsorums</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus&#39;Windel&#248;v&#39;(008BZWM)/4422">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008B ZWM/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus &#39;Windel&#248;v&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 008B ZWM)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Mangrove wood with suction cup and self-attached Microsorum</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the glass of the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus&#39;Windel&#248;v&#39;(008BZWS)/4423">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008B ZWS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus &#39;Windel&#248;v&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 008B ZWS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Mangrove wood with suction cup and self-attached Microsorum</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the glass of the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumpteropus&#39;Windel&#248;v&#39;(008B)/4418">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/008B/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum pteropus &#39;Windel&#248;v&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 008B)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very decorative when fastened to rocks or wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Not eaten by herbivorous fish</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Microsorumsp.(500OWX)/4582">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/500 OWX/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Microsorum sp.</strong><br />
                                Rhizomatous<br />
                                (Item no. 500 OWX)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Large mangrove wood with suction cups and self-attached plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the glass of the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Monosoleniumtenerum(002CTC)/18747">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/002C TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Monosolenium tenerum</strong><br />
                                Moss<br />
                                (Item no. 002C TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Intense bottle green liverwort </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Stays on the ground or may be attached to rocks or wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Previously known as Pellia</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Murdanniakeisak(135)/4763">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/135/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Murdannia keisak</strong><br />
                                Stem<br />
                                (Item no. 135)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Bamboo-like growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fast-growing, needs continuous trimming</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Replant the cut-off shoots to keep a nice group</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Myriophyllummattogrossense(037TC)/28108">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/037 TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Myriophyllum mattogrossense</strong><br />
                                Stem<br />
                                (Item no. 037 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Magnificent feathery stems</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very fast growing background plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Excellent auxiliary plant when starting an aquarium </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Myriophyllummattogrossense(037)/4454">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/037/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Myriophyllum mattogrossense</strong><br />
                                Stem<br />
                                (Item no. 037)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Magnificent feathery stems</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very fast growing background plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Excellent auxiliary plant when starting an aquarium </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Myriophyllumsp.&#39;Guyana&#39;(037ETC)/19549">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/037E TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Myriophyllum sp. &#39;Guyana&#39;</strong><br />
                                Stem<br />
                                (Item no. 037E TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Stem plant of vivid, bright green colour</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Moderate growth rate, creating many branching shoots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Suitable for nano tanks</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Nymphaealotus(019)/4432">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/019/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Nymphaea lotus</strong><br />
                                Bulb/onion<br />
                                (Item no. 019)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Eyecatching solitary plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Green or reddish brown leaves </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Bulb to be planted with the germs right above the bottom layer </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Nymphoideshydrophylla&#39;Taiwan&#39;(041BTC)/4463">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/041B TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Nymphoides hydrophylla &#39;Taiwan&#39;</strong><br />
                                Rhizomatous<br />
                                (Item no. 041B TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy, fast-growing and lush plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful, wavy leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Intense, bright green colour</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Nymphoideshydrophylla&#39;Taiwan&#39;(041B)/4462">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/041B/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Nymphoides hydrophylla &#39;Taiwan&#39;</strong><br />
                                Bulb/onion<br />
                                (Item no. 041B)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy, fast-growing and lush plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful, wavy leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Intense, bright green colour</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Phyllanthusfluitans(028TC)/22848">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/028 TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Phyllanthus fluitans</strong><br />
                                Floating plant<br />
                                (Item no. 028 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Lively red colour under strong lighting</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate in an aquarium</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Blooming flowers under the right conditions</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Pogostemondeccanensis(053FTC)/4497">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053F TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Pogostemon deccanensis</strong><br />
                                Stem<br />
                                (Item no. 053F TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Characteristic plant with coniferous stems</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Deep green colour</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to trim and maintain</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Pogostemondeccanensis(053F)/4496">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053F/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Pogostemon deccanensis</strong><br />
                                Stem<br />
                                (Item no. 053F)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Characteristic plant with coniferous stems</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Deep green colour</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to trim and maintain</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Pogostemonhelferi(053HTC)/19680">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053H TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Pogostemon helferi</strong><br />
                                Stem<br />
                                (Item no. 053H TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Carpeting foreground plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Distinctive, curly leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Also called &#39;Downoi&#39; (little star)</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Pogostemonhelferi(053HYLS)/4500">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053H YLS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Pogostemon helferi</strong><br />
                                Stem<br />
                                (Item no. 053H YLS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Lava rock with self-attached Pogostemon helferi</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Fully grown and hardy, right from the start</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to place on the bottom layer of the aquarium</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Pogostemonhelferi(053H)/4499">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053H/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Pogostemon helferi</strong><br />
                                Stem<br />
                                (Item no. 053H)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Carpeting foreground plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Distinctive, curly leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Also called &#39;Downoi&#39; (little star)</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Pogostemonstellatus(053G)/4498">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053G/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Pogostemon stellatus</strong><br />
                                Stem<br />
                                (Item no. 053G)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Magnificent stem plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Requires optimal conditions to grow well</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>May need some time to start developing optimally</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Proserpinacapalustris&#39;Cuba&#39;(037CTC)/4766">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/037C TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Proserpinaca palustris &#39;Cuba&#39;</strong><br />
                                Stem<br />
                                (Item no. 037C TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful and unique plant for any high-tech aquarium.</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful colours and an interesting leaf shape when the plant thrives.</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy to propagate by cuttings under water.</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Ranunculusinundatus(022CTC)/18225">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/022C TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Ranunculus inundatus</strong><br />
                                Stolon<br />
                                (Item no. 022C TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful umbrella-shaped, lobed leaves </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Great contrast to other leaf shapes</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Low and compact growth, will cover the bottom easily</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Riccardiachamedryfolia(003D)/4400">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/003D/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Riccardia chamedryfolia</strong><br />
                                Moss<br />
                                (Item no. 003D)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Deep green liverwort with compact growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>To be attached to rocks and pieces of wood</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Common name: Coral moss</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Ricciafluitans(001TC)/4386">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/001 TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Riccia fluitans</strong><br />
                                Moss<br />
                                (Item no. 001 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Bright green liverwort </li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Floating plant, but can be attached to rocks and wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>It often forms small, decorative oxygen bubbles on the leaf tips</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Rotalaindica&#39;Bonsai&#39;(033ETC)/4451">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/033E TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Rotala indica &#39;Bonsai&#39;</strong><br />
                                Stem<br />
                                (Item no. 033E TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Compact, with moderate growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Stem tips become reddish when exposed to high light</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Previously known as Ammania ‘Bonsai’</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Rotalamacrandra(032TC)/4445">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/032 TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Rotala macrandra</strong><br />
                                Stem<br />
                                (Item no. 032 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>One of the most outstanding, red plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Requires excellent conditions to develop its full potential</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Replant the cuttings in the substrate to create a dense group </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Rotalarotundifolia(033MP)/18810">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/033 MP/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Rotala rotundifolia</strong><br />
                                Stem<br />
                                (Item no. 033 MP)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Undemanding and easy beginner’s plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Becomes more red at high light intensity</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Multiplies easily by replanting cuttings in the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Rotalarotundifolia(033PCS)/18799">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/033 PCS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Rotala rotundifolia</strong><br />
                                Stem<br />
                                (Item no. 033 PCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Undemanding and easy beginner’s plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Becomes more red at high light intensity</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Multiplies easily by replanting cuttings in the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Rotalarotundifolia(033)/4447">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/033/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Rotala rotundifolia</strong><br />
                                Stem<br />
                                (Item no. 033)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Undemanding and easy beginner’s plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Becomes more red at high light intensity</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Multiplies easily by replanting cuttings in the bottom layer</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Rotalarotundifolia&#39;Green&#39;(033ATC)/22545">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/033A TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Rotala rotundifolia &#39;Green&#39;</strong><br />
                                Stem<br />
                                (Item no. 033A TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Its intense, bright green colour will enhance surrounding, red plants</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very dense and bushy growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Stays bright green at high light intensity</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Rotalarotundifolia&#39;H&#39;ra&#39;(032CTC)/19550">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/032C TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Rotala rotundifolia &#39;H&#39;ra&#39;</strong><br />
                                Stem<br />
                                (Item no. 032C TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful pink-orange stem plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>At high light intensity, growth may become creeping</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Branches willingly when trimmed</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Rotalawallichii(032ATC)/18748">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/032A TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Rotala wallichii</strong><br />
                                Stem<br />
                                (Item no. 032A TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Elegant stem plant with narrow leaves and red tips</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Requires perfect conditions to thrive</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Can stay low and compact if trimmed regularly</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Sagittariasubulata(079PCS)/21135">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/079 PCS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Sagittaria subulata</strong><br />
                                Stolon<br />
                                (Item no. 079 PCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Suitable for the foreground</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Depending on the conditions, the height is very varying </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Sagittariasubulata(079TC)/18270">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/079 TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Sagittaria subulata</strong><br />
                                Stolon<br />
                                (Item no. 079 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Suitable for the foreground</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Depending on the conditions, the height is very varying </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Sagittariasubulata(079)/4530">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/079/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Sagittaria subulata</strong><br />
                                Stolon<br />
                                (Item no. 079)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Suitable for the foreground</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Depending on the conditions, the height is very varying </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Schismatoglottisprietoi(102TC)/29519">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/102 TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Schismatoglottis prietoi</strong><br />
                                Stolon<br />
                                (Item no. 102 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Appears in large, dense groups</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Can resemble Anubias</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>An undemanding and easy plant</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Shinnersiarivularis&#39;Weiss-Gr&#252;n&#39;(053E)/4495">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/053E/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Shinnersia rivularis &#39;Weiss-Gr&#252;n&#39;</strong><br />
                                Stem<br />
                                (Item no. 053E)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding stem plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful marbled leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Common name “Oak leaf” due to the leaf form</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Staurogynerepens(049GPCS)/19617">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/049G PCS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Staurogyne repens</strong><br />
                                Stem<br />
                                (Item no. 049G PCS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very low and compact growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Spreads willingly creating horizontal shoots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Good light conditions will keep the growth horizontal</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Staurogynerepens(049GTC)/4482">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/049G TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Staurogyne repens</strong><br />
                                Stem<br />
                                (Item no. 049G TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very low and compact growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Spreads willingly creating horizontal shoots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Good light conditions will keep the growth horizontal</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Staurogynerepens(049G)/4481">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/049G/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Staurogyne repens</strong><br />
                                Stem<br />
                                (Item no. 049G)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Very low and compact growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Spreads willingly creating horizontal shoots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Good light conditions will keep the growth horizontal</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Taxiphyllumalternans&#39;TaiwanMoss&#39;(003CTC)/19551">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/003C TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Taxiphyllum alternans &#39;Taiwan Moss&#39;</strong><br />
                                Moss<br />
                                (Item no. 003C TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Delicate and graceful weeping moss</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>To be attached to rocks and wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Common name: Mini Taiwan Moss </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Taxiphyllumbarbieri&#39;BogorMoss&#39;(003POR)/4391">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/003 POR/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Taxiphyllum barbieri &#39;Bogor Moss&#39;</strong><br />
                                Moss<br />
                                (Item no. 003 POR)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Particularly easy and undemanding moss</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Attaches to rocks and wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Commonly named Java moss</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Taxiphyllumbarbieri&#39;BogorMoss&#39;(003TC)/4393">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/003 TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Taxiphyllum barbieri &#39;Bogor Moss&#39;</strong><br />
                                Moss<br />
                                (Item no. 003 TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Particularly easy and undemanding moss</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Attaches to rocks and wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Commonly named Java moss</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Taxiphyllumbarbieri&#39;BogorMoss&#39;(003YLS)/4394">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/003 YLS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Taxiphyllum barbieri &#39;Bogor Moss&#39;</strong><br />
                                Moss<br />
                                (Item no. 003 YLS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Particularly easy and undemanding moss</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Grown on lava rock, ready to use</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Commonly named Java moss</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Taxiphyllumsp.’FlameMoss’(003HTC)/4403">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/003H TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Taxiphyllum sp. ’Flame Moss’</strong><br />
                                Moss<br />
                                (Item no. 003H TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Deep green moss of vertical, flame like growth</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>To be attached to rocks and wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Common name ‘Flame Moss’</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Taxiphyllumsp.&#39;SpikyMoss&#39;(003GPOR)/4402">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/003G POR/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Taxiphyllum sp. &#39;Spiky Moss&#39;</strong><br />
                                Moss<br />
                                (Item no. 003G POR)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Hardy and compact moss</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives at low light</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Common name: Spiky Moss</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Taxiphyllumsp.&#39;SpikyMoss&#39;(003GTC)/18271">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/003G TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Taxiphyllum sp. &#39;Spiky Moss&#39;</strong><br />
                                Moss<br />
                                (Item no. 003G TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Hardy and compact moss</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Thrives at low light</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Common name: Spiky Moss</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Utriculariagraminifolia(049BTC)/4480">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/049B TC/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Utricularia graminifolia</strong><br />
                                Carpeting<br />
                                (Item no. 049B TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Insectivorous plant, but harmless to fishes</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Unique, but demanding foreground plant</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Beautiful green “lawn-effect”</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Advanced.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Vallisneriaamericana&#39;Gigantea&#39;(054)/4501">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/054/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Vallisneria americana &#39;Gigantea&#39;</strong><br />
                                Stolon<br />
                                (Item no. 054)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Large and fast-growing</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Is normally not eaten by herbivorous fish</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Vallisneriaspiralis&#39;Tiger&#39;(055A)/4503">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/055A/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Vallisneria spiralis &#39;Tiger&#39;</strong><br />
                                Stolon<br />
                                (Item no. 055A)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Easy and undemanding plant for beginners</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Horizontal stripes on the leaves</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Forms multiple new plant with its runners</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Easy.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Vesiculariaferriei&#39;WeepingMoss&#39;(003BPOR)/4398">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/003B POR/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Vesicularia ferriei &#39;Weeping Moss&#39;</strong><br />
                                Moss<br />
                                (Item no. 003B POR)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Moss with drooping growth and teardrop-like bright, green shoots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>To be attached to rocks and pieces of wood</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Commonly named ‘Weeping moss’</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Vesiculariaferriei&#39;WeepingMoss&#39;(003BTC)/4399">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/003B TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Vesicularia ferriei &#39;Weeping Moss&#39;</strong><br />
                                Moss<br />
                                (Item no. 003B TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Moss with drooping growth and teardrop-like bright, green shoots</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>To be attached to rocks and pieces of wood</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Commonly named ‘Weeping moss’</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Vesiculariamontagnei&#39;Christmas&#39;(003AYWS)/4397">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/003A YWS/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Vesicularia montagnei &#39;Christmas&#39;</strong><br />
                                Moss<br />
                                (Item no. 003A YWS)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Densely growing and compact moss</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Can be attached to rocks and wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Commonly named ’Christmas moss’</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Vesiculariamontagnei&#39;ChristmasMoss&#39;(003APOR)/4395">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/003A POR/2.png&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Vesicularia montagnei &#39;Christmas Moss&#39;</strong><br />
                                Moss<br />
                                (Item no. 003A POR)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Densely growing and compact moss</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Can be attached to rocks and wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Commonly named ’Christmas moss’</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        <div class="small-12 columns plant-item">
            <a href="/en/plants/plantdetails/Vesiculariamontagnei&#39;ChristmasMoss&#39;(003ATC)/4396">
                <div class="row">

                    <div class="small-12 medium-3 columns text-center">
                            <img src="https://tropica.com/imagegen.ashx?width=200&amp;image=/Plants/003A TC/2.JPG&amp;crop=resize&amp;class=product" />
                    </div>

                    <div class="small-12 medium-9 columns">
                        <div class="row" style="margin-top:50px;">
                            <div class="medium-5 small-5 columns plantGallaryItemName">
                                <strong>Vesicularia montagnei &#39;Christmas Moss&#39;</strong><br />
                                Moss<br />
                                (Item no. 003A TC)
                               
                            </div>
                            <div class="medium-6 small-6 columns plantGallaryItemDesc">
                                <div class="plant-description">
                                    
                                    <ul class="fa-ul">
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Densely growing and compact moss</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Can be attached to rocks and wood pieces</li>
                                            <li><span class="fa-li"><i class="fas fa-angle-left"></i></span>Commonly named ’Christmas moss’</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="small-1 medium-1 columns text-center">
                                
                                <img src="/Graphics/Web/icon_difficulty_Medium.png" class="icon_difficulty_medium" />
"""


# Parsing content
soup = BeautifulSoup(html_content, "html.parser")

# Find 'plant-item' elements
plant_items = soup.find_all("div", class_="plant-item")

# Initialize an empty list to store extracted data
table_data = []

# Loop through each 'plant-item'
for plant_item in plant_items:
    # Check if the 'div' contains a link
    link_element = plant_item.find("a")
    if link_element:
        # Extract the link
        link = link_element["href"]
        link_completo = "https://tropica.com/" + link
        print(f"Link trovato: {link_completo}")
    else:
        # No link present
        print("Nessun link trovato in questo elemento")
        link_completo = None

    # Find the 'strong' tag within the 'div' with the class 'plantGallaryItemName'
    plant_name_element = plant_item.find(class_="plantGallaryItemName").find("strong")

    if plant_name_element:
        # Extract the text from the 'strong' tag
        plant_name = plant_name_element.text.strip()
        print(f"Nome della pianta: {plant_name}")
    else:
        # No 'strong' element found
        print("Nessun elemento 'strong' trovato.")
        plant_name = None

    # Check if the image element exists before trying to find the image link
    image_element = plant_item.find("div", class_="small-12 medium-3 columns text-center")
    if image_element:
        # Find the 'img' tag within the image element
        image = image_element.find("img")
        if image:
            # Extract the image link if the image exists
            image_link = image["src"]
            print(f"Link immagine: {image_link}")
        else:
            # No image found within the image element
            print("Nessuna immagine trovata in questo elemento")
            image_link = None
    else:
        # No image element found
        print("Nessuna immagine trovata in questo elemento")
        image_link = None

    # Add data to the list only if all three elements are found
    if link_completo and plant_name and image_link:
        table_data.append([plant_name, link_completo, image_link])

# Check if table data is not empty (avoid empty DataFrame creation)
if len(table_data) > 0:
    # Create the DataFrame
    plant_data = pd.DataFrame(table_data, columns=["Nome Pianta", "Link", "Link Immagine"])

    # Print the DataFrame (optional)
    print(plant_data.to_string())

    # Save the DataFrame to an Excel file (optional)
    plant_data.to_excel("D:\\informatica\\data_piante_link_img.xlsx", index=False)

else:
    print("Nessun dato trovato.")
