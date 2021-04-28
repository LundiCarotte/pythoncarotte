# -*-coding:utf-8 -*
""" module contenant les styles nécessaires à la génération du template html"""

class Tag:
    """Classe définissant le style du contenu des blocs d'un article (texte, légendes, citations, sous-titres...)"""

    def __init__(self):

        self.texte_entree = """
        <!-- on débute un bloc de texte -->

        <tr>
          <td
             align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;"
          >

            <div
              style="font-family:Libre Baskerville, Helvetica, Arial, sans-serif;font-size:13px;line-height:24px;text-align:left;color:#000000;"
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



        self.sous_titre_entree =  """
        <!--début sous-titre-->
        <tr>
          <td align="left" style="font-size:0px;padding:40px 5px 10px;word-break:break-word;">

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

            <a style="font-size:10px" href="http://www.facebook.com/sharer.php?u=URL&t=CIT_URL" style="text-decoration:none" target="blank">
              <img alt="FB" style="border:0" height="25" width="15" src="https://lundicarotte.fr/img/facebook-couleur.png">
            </a> &nbsp;
            <a style="font-size:10px" href="http://twitter.com/share?url=URL&text=CIT_URL" style="text-decoration:none" target="blank">
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
