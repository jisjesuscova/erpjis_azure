<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <style type="text/css">
            body {
                font-family: Arial, Helvetica, sans-serif;
            }
        </style>
    </head>
    <body>
        <table class="table table-bordered" style="width:100%;">
            <thead>
                <tr>
                    <img style="width: 80px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/logo.png'))) }}"> 
                </tr>
            </thead>
        </table>
        <table class="table table-bordered" style="width:100%;">
            <thead>
                <tr>
                    <td><h3><font style="font-family:arial;"><center> CARTA DE FELICITACIONES</center></font></h3></td>   
                </tr>
            </thead>
        </table>
        <hr>
        <table class="table" style="width:100%;">
            <tbody>
                <tr>
                    <td style="text-align: justify;">
                        Con mucha alegría le hacemos llegar a usted <strong>{{ $full_name }}</strong> esta carta con la finalidad de darles las gracias y felicitarle por el esmero,
                        dedicación y los buenos resultados que ha obtenido, esta vez destacamos: <strong>{{ $congratulation_description }}</strong>.<br><br>
                        Usted ha logrado demostrar una destacada participación y compromiso con JIS Parking, lo cual nos llena de orgullo, porque
                        nos demuestra su aprecio y dedicación por la organización.<br><br>
                        Sabemos que sería imposible alcanzar nuestros objetivos sin Usted, y es por eso que nos complace el esfuerzo y el
                        compromiso que demuestra día a día en su lugar de trabajo. De parte de la gerencia y toda la organización le agradecemos y le
                        felicitamos por su excelente labor. Esperamos que usted pueda seguir siendo un ejemplo a seguir y una motivación para todo
                        nuestro equipo de trabajo. Deseamos que se mantenga con la misma actitud y compromiso.<br><br>
                        
                        Saludos a usted.

                        <br><br><br><br><br><br>

                        <center><img style="width: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____________________</center>
                        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
                        <center>76.063.822-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}&nbsp;&nbsp;</center>
                    </td>
                </tr>
            </tbody>
        </table>
     </body>
</html>