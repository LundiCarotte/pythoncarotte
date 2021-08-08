# -*-coding:utf-8 -*
""" module contenant les classes nécessaires à la génération du template html"""

from .classeBloc import *
from .variables import *

def creerBloc(i):
    """ Prend en argument le nom d'un bloc de l'article, et renvoie un objet Bloc contenant les informations utiles à la création du code HTML de ce bloc"""

    # on crée un objet Bloc vide
    x = Bloc()

    # définition bloc logo
    if i == logo:
        x.a = False
        x.nom = i
        x.repereHtml = "<!--LOGO-->"
        x.code = """
      <tr>
        <td
        align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;"
        >

        <table
        border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;margin-bottom: 60px;"
        >
        <tbody>
          <tr>
            <td  style="width:170px;">

              <a
              href="https://lundicarotte.fr" target="_blank"
              >

              <img
              alt="Logo" height="auto" src="https://lundicarotte.fr/img/logo.png" style="border:none;display:block;outline:none;text-decoration:none;height:auto;width:100%;" title="" width="170"
              />

            </td>
          </tr>
        </tbody>
      </table>

      </td>
      </tr>
    """

    # définition bloc donheader
    if i == donheader:
        x.a = False
        x.nom = i
        x.repereHtml = "<!--DONHEADER-->"
        x.code = """
      <tr>
        <td align="center" style="font-size:0px;word-break:break-word">
          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#ffffff;background-color:#ffffff;width:100%;">
            <tbody>
              <tr>
                <td style="direction:ltr;font-size:0px;padding:0px;text-align:center;">
                <!--[if mso | IE]>
                <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                  <tr>
                    <td class="" style="vertical-align:top;width:510px;">
                <![endif]-->

                <div style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:85% !important;max-width:85%;">
                  <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
                    <tbody>
                      <tr>
                        <td style="vertical-align:top;padding:0px 25px 10px;padding-right:0px;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="" width="100%">
                            <tbody>
                              <tr>
                                <td align="left" style="font-size:0px;padding:0px;word-break:break-word;">
                                  <div style="font-family:Helvetica, Arial, sans-serif;font-size:11px;line-height:20px;text-align:left;color:#000000;">
                                    <a href="https://lundicarotte.fr/don" style="color: black; text-decoration: none;" target="_blank">
                                      LundiCarotte est un projet gratuit, associatif et indépendant. Nous dépendons des dons de nos lecteurs et lectrices pour financer nos locaux et développer nos activités. Si vous aimez nous lire, vous pouvez nous soutenir. Merci !
                                    </a>
                                  </div>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!--[if mso | IE]>
                  </td>
                <td class="" style="vertical-align:top;width:90px;">
                <![endif]-->

                <div class="mj-column-per-15 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:15% !important;max-width:15%;">
                  <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
                    <tbody>
                      <tr>
                        <td style="vertical-align:top;padding:0px 25px;padding-left:0px;">
                          <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="" width="100%">
                            <tbody>
                              <tr>
                                <td align="right" style="font-size:0px;padding:0px;word-break:break-word;">
                                  <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                    <tbody>
                                      <tr>
                                        <td style="width:65px;">
                                          <a href="https://lundicarotte.fr/don" target="_blank">
                                            <img height="auto" src="http://localhost:8000/api/admin/media//img/commentaire.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="65">
                                          </a>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!--[if mso | IE]>
                    </td>
                  </tr>
                </table>
                <![endif]-->
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
      <tr>
        <td style="font-size:0px;word-break:break-word;background:#F5F5F5;">
          <!--[if mso | IE]>
          <table role="presentation" border="0" cellpadding="0" cellspacing="0">
            <tr>
              <td height="12" style="vertical-align:top;height:12px;">
          <![endif]-->
          
          <div style="height:12px;">
            &nbsp;
          </div>
          
          <!--[if mso | IE]>
              </td>
            </tr>
          </table>
          <![endif]-->
        </td>
      </tr>
    """

    # définition du bloc du titre
    if i == titre:
        x.nom = i
        x.repereTexte = "TITRE-PAGE"
        x.repereHtml = "<!--TITRE-->"
        x.codeAvant = """
                <tr>
                  <td
                  align="left" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-bottom:40px;word-break:break-word;"
                  >

                  <div
                  style="font-family:Libre Baskerville, Helvetica, Arial, sans-serif;font-size:13px;line-height:50px;text-align:left;color:#000000;"
                  >
                  <h1 style="font-family: Libre Baskerville, Helvetica, Arial, sans-serif; font-size: 28px; font-weight: normal;">
                    <span style="color:#000000">
                      <span style="font-size:44px">
                        <span style="font-family:Libre Baskerville,Helvetica,Arial,sans-serif">
                """
        x.codeApres = """
                        </span>
                      </span>
                    </span>
                  </h1>
                </div>

                </td>
                </tr>
                """

    # définition du bloc date
    if i == date:

        x.nom = i
        x.repereTexte = "DATE-ARTICLE"
        x.repereHtml = "<!--DATE-->"
        x.codeAvant = """
                <tr>
                  <td
                     align="left" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-bottom:20px;word-break:break-word;"
                  >

                <div
                style="font-family:Libre Baskerville, Helvetica, Arial, sans-serif;font-size:13px;line-height:24px;text-align:left;color:#000000;"
                >
                <p style="font-size: 18px; font-family: Libre Baskerville, Helvetica, Arial, sans-serif; color: #000000; line-height: 23px; text-align: right; margin: 10px 0;">
                <span style="color:#000000">
                <span style="font-size:13px">
                <span style="font-family:Libre Baskerville,Helvetica,Arial,sans-serif">
                <span style="font-weight: bold">
                """
        x.codeApres = """
                </span>
                </span>
                </span>
                </span>
                </p>
                </div>

                  </td>
                </tr>
                """

    # définition bloc image
    if i == image:
        x.nom = i
        x.a = False
        x.repereTexte = "URL-IMAGE"
        x.repereHtml = "<!--IMAGE-->"
        x.code = """
        <!--début image-->
        <tr>
        <td
        align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;"
        >

        <table
        border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;"
        >
        <tbody>
        <tr>
        <td  style="width:300px;">

        <img
        alt="Illustration" height="auto" src="url_Image" style="border:none;display:block;outline:none;text-decoration:none;height:auto;width:100%;" title="" width="300"
        />

        </td>
        </tr>
        </tbody>
        </table>

        </td>
        </tr>
        <!--fin image-->

        """

    # définition du bloc intro
    if i == intro:

        x.nom = i
        # bloc plus complexe à génerer que le bloc titre (par exemple)
        x.a = False

        x.repereTexte1 = "INTRODUCTION"
        x.repereTexte2 = "DÉVELOPPEMENT"
        x.repereHtml = "<!--INTRO-->"
        x.codeAvant = tag.texte_entree
        x.codeApres = tag.texte_sortie

    # définition du bloc développement
    if i == dev:

        x.nom = dev
        x.a = False

        x.repereTexte1 = "DÉVELOPPEMENT"
        x.repereTexte2 = "CONCLUSION"
        x.repereHtml = "<!--DÉVELOPPEMENT-->"
        x.codeAvant = tag.texte_entree
        x.codeApres = tag.texte_sortie

    # définition du bloc conclusion
    if i == outro:

        x.nom = i
        x.a = False

        x.repereTexte1 = "CONCLUSION"
        x.repereTexte2 = "FIN"
        x.repereHtml = "<!--CONCLUSION-->"
        x.codeAvant = tag.texte_entree
        x.codeApres = tag.texte_sortie


    # définition du bloc auteurs
    if i == auteurs:
        x.a = False
        x.nom = i
        x.repereTexte = "AUTEURS"
        x.repereHtml = "<!--AUTEURS-->"
        x.codeAvant = """
                <tr>
                  <td
                     align="left" style="font-size:0px;padding:20px 25px 10px;word-break:break-word;"
                  >

                <div
                style="font-family:Libre Baskerville, Helvetica, Arial, sans-serif;font-size:13px;line-height:22px;text-align:left;color:#000000;"
                >
                <p style="font-size: 18px; font-family: Libre Baskerville, Helvetica, Arial, sans-serif; color: #000000; line-height: 23px; text-align: right; margin: 10px 0;">
                <span style="font-family:Arial,sans-serif">
                """
        x.codeApres = """
                </span></p>
                </div>

                  </td>
                </tr>
                """

    if i == partage:
        x.a = False
        x.nom = i
        x.repereHtml = "<!--PARTAGE-->"
        x.code =  """
                  <!-- Début liens de partage -->
                  <tr>
                                <td style="word-wrap:break-word;font-size:0px;padding-top:40px" align="center"; padding:60px>
                                  <table style="border-collapse:separate;" align="center" >
                                    <tbody>
                                      <tr>
                                        <td style="border:0px solid #000000;color:#000000;background-color:#ffffff;cursor:auto;padding:3px;" align="center" valign="middle" >
                                          <center><a style="text-decoration:none;background:transparent;font-size:10px;line-height:120%;margin:0px;">
                                          <i>&nbsp;&nbsp;&nbsp;Partager ce LundiCarotte&nbsp;&nbsp;&nbsp;</i></a></center>
                                        </td>
                                      </tr>

                                    </tbody>
                                  </table>
                                </td>
                              </tr>

                          <tr>
                            <td>
                              <center><a href="https://www.facebook.com/sharer/sharer.php?u=_URL_"><img alt="" title="" height="auto" src="https://lundicarotte.fr/api/admin/media/img/facebook.png" width="100"></a>
                              <a href="mailto:?subject=Un peu de lecture&body=Voici un lien vers un article qui devrait te plaire _URL_"><img alt="" title="" height="auto" src="https://lundicarotte.fr/api/admin/media/img/mail.png"  width="100"></a>
                              <a href="https://twitter.com/share?url=_URL_&text=Un%20petit%20peu%20de%20lecture%20aujourd%20hui%20avec%20un LundiCarotte%20a%20lire%20et%20a%20relire&via=lundicarotte"
                              ><img alt="" title="" height="auto" src="https://lundicarotte.fr/api/admin/media/img/twitter.png"  width="100"></a></center>
                            </td>
                          </tr>
                          <!-- fin liens de partage -->
                        """

    if i == don:
        x.a = False
        x.nom = i
        x.repereHtml = "<!--CaseDon-->"
        x.code = """
                    <tr height="30px"></tr>
                    <!-- DÉBUT CASE DON -->
                    <tr>
                      <td style="padding:30px;background-color:#ffffff;">
                        <table style="margin-left:25px; margin-right:25px ">
                          <tbody>


                            <tr>
                              <td>
                                <table >
                                  <tbody>


                                    <tr>
                                      <td style="font-family:Libre Baskerville ;color:#000000" width="1000px"></p>LundiCarotte est un projet <b>gratuit</b>,<b> associatif</b> et <b>indépendant</b>. <br/>Si l'on vous plaît, vous pouvez nous soutenir.</p> </td>

                                    </tr>





                                    <!-- Bouton Don -->
                                    <tr>
                                      <td style="word-wrap:break-word;padding:5px" align="center">
                                        <table  cellpadding="0" cellspacing="0" style="border-collapse:separate;" align="center" border="0">
                                          <tbody>
                                            <tr>
                                              <td style="border:2px solid #000000;border-radius:40px;color:#000000;background-color:#ffffff;cursor:auto;padding:3px;" align="center" valign="middle" >
                                                <a style="text-decoration:none;background:transparent;font-family:Arial, sans-serif;font-size:18px;font-weight:bold;line-height:120%;margin:0px;text-decoration:none;color:#000000" href="https://www.lundicarotte.fr/don">&nbsp;&nbsp;&nbsp;<b>FAIRE UN DON</b>&nbsp;&nbsp;&nbsp;</a>
                                              </td>
                                            </tr>
                                          </tbody>
                                        </table>
                                      </td>
                                    </tr>
                                    <!--Fin bouton don-->

                                  </tbody>
                                </table>
                              </td>
                            </tr>


                          </tbody>
                        </table>
                      </td>
                    </tr>

        <!--FIN DE LA CASE DON-->

        """

    if i == actu:
        x.nom = i
        x.a = False
        x.repereTexte = "ACTU"
        x.repereJc = "JEUDICAROTTE"
        x.repereHtml = "<!--CaseActu-->"
        x.case_actu_entree = """
                    <tr><td>&nbsp;</td></tr>

                    <!-- Case ActU -->

                    <tr>
                      <td style="padding:30px;padding-bottom:0px;background-color:#ffffff;" align="center">
                        <table style="margin-left:25px; margin-right:25px ">
                          <tbody>
                            <tr>
                              <td >
                                <table >
                                  <tbody>
                                    <tr><!-- Titre ActU -->
                                      <td style="padding:10px" >
                                        <table >
                                          <tbody>
                                            <tr>

                                              <td><a style="text-decoration:none;background:transparent;font-family:Arial, sans-serif;font-size:18px;line-height:120%;text-transform:none;margin:0px;">
                                                <b>&nbsp;ACTU&nbsp;</b></a>
                                              </td>

                                            </tr>
                                          </tbody>
                                        </table>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>

                    <!-- Case ActU 2 -->
                    <tr>
                      <td style="padding:30px;background-color:#ffffff;font-size:13px;" align="left"  >
                        <table style="margin-left:25px; margin-right:25px" >
                          <tbody>
                            <tr>
                              <td>
                                <table>
                                  <tbody>

        """
        x.case_actu_sortie = """
                                  </tbody>
                                </table>
                              </td>
                            </tr>


                          </tbody>
                        </table>
                      </td>
                    </tr>
        <!--FIN CASE ACTU-->
        """

        x.texte_actu_entree = """
                                    <tr>
                                      <td style="font-family:Libre Baskerville ;color:#000000">

        """

        x.texte_actu_sortie = """
                                       <br/><br/>
                                      </td>
                                    </tr>
                  			    				<tr>
                  			    					<td>
                  			    						<p style="margin:0px auto;border-top:3px solid #000000;width:100%;">
                  			    						</p>
                  			    						<br/>
                  			    					</td>
                                    </tr>

        """

        x.texte_jc = """

                                    <tr>
                                      <td style="font-family:Libre Baskerville ;color:#000000">

                                       Gagnant_1 de <a target="_blank" href="Lien_JC" style="text-decoration: none; color: #E36C0A;">JeudiCarotte</a> n'est autre que Gagnant_2, qui remporte donc une bonne tablette de chocolat. Nous l'invitons à nous envoyer par e-mail son adresse postale.<br/><br/>
                                      </td>
                                    </tr>
                                   		<tr>
                                   			<td>
                                   				<p style="margin:0px auto;border-top:3px solid #000000;width:100%;">
                                   				</p>
                                   			</td>
                                    	</tr>
        """

    # définition bloc courrier
    if i == courrier:
        x.nom = i
        x.a = False
        x.repereHtml = "<!--CaseCourrier-->"
        x.question = "QUESTION"
        x.reponse = "REPONSE"

        x.case_courrier_entree = """
        <tr><td>&nbsp;</td></tr>

                <!-- Case Courrier -->
                <tr>
                  <td style="padding:30px;background-color:#ffffff;"align="center">
                    <table style="margin-left:25px; margin-right:25px ">
                      <tbody>


                        <tr>
                          <td>
                            <table align="center" >
                              <tbody>
                                <tr><!-- Titre A propos -->
                                  <td style="word-wrap:break-word;font-size:0px" align="center">
                                    <table style="border-collapse:separate;" align="center" >
                                      <tbody>
                                        <tr>
                                          <td align="center">
                                            <center><img alt="" title="" height="auto" src="https://lundicarotte.fr/api/admin/media/img/commentaire.png"  width="150"></center></td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                            <tr>
                              <td align="center">
                                <table >
                                  <tbody>

                                    <tr><!-- Titre Courrier -->
                                      <td style="padding:10px" >
                                        <table >
                                          <tbody>
                                            <tr>

                                            <td><a style="text-decoration:none;background:transparent;font-family:Arial, sans-serif;font-size:18px;line-height:120%;text-transform:none;margin:0px;">
                                              <b>&nbsp;LE COURRIER&nbsp;</b></a>
                                            </td>

                                          </tr>
                                          </tbody>
                                        </table>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </td>
                            </tr>
                          <tr>
                            <td align="left">
                              <table >
                                <tbody>
                                  <tr>
                                    <td style="word-wrap:break-word;font-size:0px" align="left">
                                      <table style="border-collapse:separate;" align="left" >
                                        <tbody>
        """

        x.case_courrier_sortie = """

                                          </tbody>
                                        </table>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </td>
                            </tr>


                          <tr>
                            <td align="center">
                              <table >
                                <tbody>
                                  <tr><!-- Titre A propos -->
                                    <td style="word-wrap:break-word;font-size:0px" align="center">
                                      <table style="border-collapse:separate;" align="center" >
                                        <tbody>
                                          <tr>
                                            <td style="border:2px solid #000000;border-radius:40px;color:#000000;background-color:#ffffff;cursor:auto;padding:3px;" align="center" valign="middle" >
                                              <center><a style="text-decoration:none;background:transparent;font-family:Arial, sans-serif;font-size:18px;font-weight:bold;line-height:120%;margin:0px;text-decoration:none;color:#000000" href="mailto:hello@lundicarotte.fr?subject=Bonjour les LundiCarottes&nbsp;!">
                                                <b>&nbsp;&nbsp;&nbsp;ENVOYER DU COURRIER&nbsp;&nbsp;&nbsp;</b></a></center>
                                              </td>
                                            </tr>

                                          </tbody>
                                        </table>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                    <!--fin case courrier-->

                    """
        x.texte_qr_1 = """
                                      <tr>
                                        <td style="font-family:Libre Baskerville ;color:#000000;font-size:13px;">
        """

        x.texte_qr_2 = """
                                          <br/>
                                          <br/><i>
        """

        x.texte_qr_3 = """

        </i><br/><br/>
        """

        x.texte_qr_4 = """
        </td>
        </tr>
        """

    if i == quizz:
        x.a = False
        x.nom = i
        x.repereTexte = "QUIZZ"
        x.repereHtml = "<!--CaseQuizz-->"
        x.code = """


          <tr><!-- Case Quizz -->
            <td style="padding:30px;background-color:#ffffff;" align="center">
              <table style="margin-left:25px; margin-right:25px ">
                <tbody>




                  <tr>
                    <td
                    align="center" style="background:#ffffff;font-size:0px;padding:10px 25px;word-break:break-word;"
                    >

                    <table
                    border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;"
                    >
                    <tbody>
                      <tr>
                        <td  style="width:300px;">

                          <a
                          href="url_quizz" target="_blank"
                          >

                          <img
                          alt="" height="auto" src="https://lundicarotte.fr/api/admin/media/img/quizz-explication.png" style="border:none;display:block;outline:none;text-decoration:none;height:auto;width:100%;" title="" width="300"
                          />

                        </a>

                      </td>
                    </tr>
                  </tbody>
                </table>

              </td>
            </tr>

            <tr>
              <td align="center">
                <table >
                  <tbody>
                    <tr><!-- Titre A propos -->
                      <td style="word-wrap:break-word;font-size:0px" align="center">
                        <table style="border-collapse:separate;" align="center" >
                          <tbody>
                            <tr>
                              <td style="border:2px solid #000000;border-radius:40px;color:#000000;background-color:#ffffff;cursor:auto;padding:3px;" align="center" valign="middle" >
                                <center><a style="text-decoration:none;background:transparent;font-family:Arial, sans-serif;font-size:18px;font-weight:bold;line-height:120%;margin:0px;text-decoration:none;color:#000000" href="url_quizz">
                                  <b>&nbsp;&nbsp;&nbsp;LE QUIZZ&nbsp;&nbsp;&nbsp;</b></a></center>
                                </td>
                              </tr>

                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
            </tbody>
          </table>
          </td>
          </tr>


        """


    if i == pied:
        x.a = False
        x.nom = i
        x.repereHtml = "<!--PiedPage-->"
        x.code = """
         <tr><td>&nbsp;</td></tr>

                          <!-- Case Bas de page -->
                          <tr>
                            <td style="padding:10px;background-color:#000000;">
                              <table style="margin-left:25px; margin-right:25px ">
                                <tbody>




                                  <tr>
                                    <td>
                                      <table >
                                        <tbody>


                                          <tr>
                                            <td style="text-align: left;">

                                              <div class="mj-column-per-100 outlook-group-fix" style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%;"><table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0"><tbody>

                                                <tr><td style="word-wrap:break-word;background:#000000;font-size:0px;padding:0px 20px 0px 20px;padding-top:0px;padding-bottom:0px;" align="center" background="#000000"><div style="cursor:auto;color:#9399a1;font-family:Arial, sans-serif;font-size:11px;line-height:22px;text-align:center;"><style></style><p style="margin: 10px 0;">
                                                  <img src="https://lundicarotte.fr/img/logoblanc.png" width="170" alt="logo-blanc"></td></tr>


                                                  <tr><td style="word-wrap:break-word;background:#000000;font-size:0px;padding:0px 20px 0px 20px;padding-top:0px;padding-bottom:0px;" align="center" background="#000000"><div style="cursor:auto;color:#9399a1;font-family:Arial, sans-serif;font-size:11px;line-height:22px;text-align:center;"><style></style><p style="margin: 10px 0;"><span style="color:#ffffff">Cet email a été envoyé à l'adresse [[EMAIL_TO]], <a href=[[UNSUB_LINK_FR]] style="text-decoration:none;  font-family:'Helvetica','Arial',sans-serif;  color:#ffffff;" target="blank">cliquez ici</a> pour annuler votre abonnement.</span></p></div></td></tr><tr>
                                                  <td style="word-wrap:break-word;background:#000000;font-size:0px;padding:0px 20px 0px 20px;padding-top:0px;padding-bottom:0px;" align="center" background="#000000"><div style="cursor:auto;color:#9399a1;font-family:Arial, sans-serif;font-size:11px;line-height:22px;text-align:center;"><style></style><p style="margin: 10px 0;"><span style="color:#ffffff">
                                                    Pour être sûr de recevoir nos prochaines éditions directement dans votre boîte de réception, nous vous invitons à ajouter manuellement l'adresse email « hello@lundicarotte.fr » dans votre carnet d'adresse. Pour tout problème de réception, n'hésitez pas à communiquer avec nous en répondant à cet email.</span></p></div></td></tr><tr>

                                                    <td style="word-wrap:break-word;background:#000000;font-size:0px;padding:0px 20px 0px 20px;padding-top:0px;padding-bottom:0px;" align="center" background="#000000"><div style="cursor:auto;color:#9399a1;font-family:Arial, sans-serif;font-size:11px;line-height:22px;text-align:center;"><style></style><p style="margin: 10px 0;"><span style="color:#ffffff">LundiCarotte.fr - Association LundiCarotte - Paris</span></p></div></td></tr></tbody></table></div>

                                                  </td>
                                                </tr>



                                              </tbody>
                                            </table>
                                          </td>
                                        </tr>


                                      </tbody>
                                    </table>
                                  </td>
                                </tr>

        """




    return(x)
