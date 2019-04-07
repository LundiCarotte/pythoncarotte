# -*-coding:utf-8 -*
""" module contenant les styles nécessaires à la génération du template html"""

class Tag:
    """Classe définissant le style du texte d'un article"""

    def __init__(self):

        self.texte_entree = """
        <!-- on débute un bloc de texte -->

        <tr>
          <td
             align="left" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-bottom:0px;word-break:break-word;"
          >

            <div
              style="font-family:Libre Baskerville, Helvetica, Arial, sans-serif;font-size:13px;line-height:24px;text-align:justify;color:#000000;"
            >
              <p style="font-size: 18px; font-family: Helvetica, Arial, sans-serif; color: #000000; line-height: 20px; margin: 0px 0;">
        """

        self.texte_sortie = """
        <!-- on termine un bloc de texte -->

              </p>
            </div>

          </td>
        </tr>
        """

        self.titre_entree = """
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

        self.titre_sortie = """
                </span>
              </span>
            </span>
          </h1>
        </div>

        </td>
        </tr>
        """

        self.date_entree = """
        <tr>
          <td
             align="left" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-bottom:0px;word-break:break-word;"
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
        self.date_sortie = """
        </span>
        </span>
        </span>
        </span>
        </p>
        </div>

          </td>
        </tr>

        """

        self.image = """
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

        self.image_sup = """
        <!--début image sup-->
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
        alt="Illustration" height="auto" src="AJOUT-IMAGE" style="border:none;display:block;outline:none;text-decoration:none;height:auto;width:100%;" title="" width="300"
        />

        </td>
        </tr>
        </tbody>
        </table>

        </td>
        </tr>
        <!--fin image sup-->

        """


        self.legende_entree = """
        <!--début légende-->
        <tr>
          <td
             align="left" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-bottom:0px;word-break:break-word;"
          >

        <div
        style="font-family:Libre Baskerville, Helvetica, Arial, sans-serif;font-size:13px;line-height:24px;text-align:left;color:#000000;"
        >
        <p style="font-size: 18px; font-family: Libre Baskerville, Helvetica, Arial, sans-serif; color: #000000; line-height: 23px; text-align: center; margin: 10px 0;">
        <span style="font-size:15px">


        """

        self.legende_sortie = """

        </span>
        </p>
        </div>

          </td>
        </tr>

        <!--fin légende -->

        """

        self.carotte = """
        <tr>
          <td
             align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;"
          >

        <table
        border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;"
        >
        <tbody>
        <tr>
        <td  style="width:10px;">

        <img
        alt="" height="auto" src="https://lundicarotte.fr/api/admin/media/img/carotte.png" style="border:none;display:block;outline:none;text-decoration:none;height:auto;width:100%;" title="" width="10"
        />

        </td>
        </tr>
        </tbody>
        </table>

          </td>
        </tr>
        """

        self.auteurs_entree = """
        <tr>
          <td
             align="left" style="font-size:0px;padding:10px 25px;padding-top:10px;padding-bottom:0px;word-break:break-word;"
          >

        <div
        style="font-family:Libre Baskerville, Helvetica, Arial, sans-serif;font-size:13px;line-height:22px;text-align:left;color:#000000;"
        >
        <p style="font-size: 18px; font-family: Libre Baskerville, Helvetica, Arial, sans-serif; color: #000000; line-height: 23px; text-align: right; margin: 10px 0;">
        <span style="font-family:Arial,sans-serif">
        """

        self.auteurs_sortie = """
        </span></p>
        </div>

          </td>
        </tr>
        """

        self.contributeurs_entree = """
        <tr>
          <td
             align="left" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-bottom:0px;word-break:break-word;"
          >

        <div
        style="font-family:Libre Baskerville, Helvetica, Arial, sans-serif;font-size:13px;line-height:22px;text-align:left;color:#000000;"
        >
        <p style="font-size: 18px; font-family: Libre Baskerville, Helvetica, Arial, sans-serif; color: #000000; line-height: 23px; text-align: right; margin: 10px 0;">
        <span style="font-family:Arial,sans-serif">
        """

        self.contributeurs_sortie = """
        </span></p>
        </div>

          </td>
        </tr>
        """

        self.partage = """

                          <!-- Début liens de partage -->
                          <tr>
                                        <td style="word-wrap:break-word;font-size:0px;padding-top:40px" align="center">
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

        self.case_quizz = """


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

        self.don = """
                    <tr height="30px"></tr>
                    <!-- Case Don -->
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

        self.case_actu_entree = """
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

        self.case_actu_sortie = """
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

        self.texte_actu_entree = """
                                    <tr>
                                      <td style="font-family:Libre Baskerville ;color:#000000">

        """

        self.texte_actu_sortie = """
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

        self.texte_jc = """

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

        self.case_courrier_entree = """
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

        self.case_courrier_sortie = """

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
        self.texte_qr_1 = """
                                      <tr>
                                        <td style="font-family:Libre Baskerville ;color:#000000;font-size:13px;">
        """

        self.texte_qr_2 = """
                                          <br/>
                                          <br/><i>
        """

        self.texte_qr_3 = """

        </i><br/><br/>
        """

        self.texte_qr_4 = """
        </td>
        </tr>
        """

        self.pied = """
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


                                                  <tr><td style="word-wrap:break-word;background:#000000;font-size:0px;padding:0px 20px 0px 20px;padding-top:0px;padding-bottom:0px;" align="center" background="#000000"><div style="cursor:auto;color:#9399a1;font-family:Arial, sans-serif;font-size:11px;line-height:22px;text-align:center;"><style></style><p style="margin: 10px 0;"><span style="color:#ffffff">Cet email a été envoyé à l'adresse [[EMAIL_TO]], <a href=[[UNSUB_LINK_FR]] style="text-decoration:none;  font-family:'Helvetica','Arial',sans-serif;  color:#ffffff; target="blank" ">cliquez ici</a> pour annuler votre abonnement.</span></p></div></td></tr><tr>
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

        self.sous_titre_entree =  """

        <!--début sous-titre-->

        <tr>
          <td
          align="left" style="font-size:0px;padding:10px 5px;padding-top:0px;padding-bottom:0px;word-break:break-word;"
          >

          <h3 style="font-size: 18px; font-weight: bold; font-family: Libre Baskerville, Helvetica, Arial, sans-serif; color: #000000; text-align: center;">
          """

        self.sous_titre_sortie = """

              </h3>

            </td>
            </tr>
            <!--fin sous-titre-->

            """

        self.citation = """

        <!--début bloc citation-->

        <tr>
            <td
               align="right" style="font-size:32px;color:#E36C0A;padding:10px 25px;padding-top:0px;padding-bottom:0px;word-break:break-word;"
            >

            <br/>
            <center><b>«&nbsp;CITATION&nbsp;»<br/></b></center>

            <a style="font-size:10px" href="http://www.facebook.com/sharer.php?u=URL&t=CITATION" style="text-decoration:none" target="blank">
              <img alt="FB" style="border:0" height="25" width="15" src="https://lundicarotte.fr/img/facebook-couleur.png">
            </a> &nbsp;
            <a style="font-size:10px" href="http://twitter.com/share?url=URL&text=CITATION" style="text-decoration:none" target="blank">
              <img alt="TW" style="border:0" height="25" width="25" src="https://lundicarotte.fr/img/twitter-couleur.png">
            </a>
          </td>

        </tr>

        <!--fin bloc citation-->
        """

        self.spacer = """

        <!--Début SPACER-->

        <tr>
          <td
             style="font-size:0px;word-break:break-word;"
          >


        <!--[if mso | IE]>

        <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td height="20" style="vertical-align:top;height:20;">

        <![endif]-->

        <div
        style="height:20;"
        >
        &nbsp;
        </div>

        <!--[if mso | IE]>

        </td></tr></table>

        <![endif]-->


          </td>
        </tr>

        <!--Fin SPACER-->


        """



#       self. = """
#
#        """


tag = Tag()
