<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <style type="text/css">
            body {
                font-family: Arial, Helvetica, sans-serif;
            }
            .page-break {
                page-break-after: always;
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
                    <td><h3><center>CAMBIO DE SUCURSAL</center></h3></td>   
                </tr>
            </thead>
        </table>
        <hr>
        <table class="table" style="width:100%;">
            <tbody>
                <tr>
                    <td style="text-align: justify;">
                        Por medio del presente documento se deja constancia que el trabajador Sr(a) <strong>{{ $full_name }}</strong>, cédula de identidad Nº <strong>{{ $rut }}</strong>, que en virtud a lo dispuesto en el artículo 12 del Código del Trabajo,
                        a contar del día <strong>{{ $start_date }}</strong>, las funciones que presta como <strong>{{ $position }}</strong>, deberán ejecutarse en la
                        sucursal <strong>{{ $branch_office_name }}</strong>, ubicada en <strong>{{ $branch_office_address }}</strong>.<br><br>
                        En virtud de la experiencia adquirida durante los años trabajando con nosotros, hemos visto que usted posee las cualidades
                        necesarias como para ser elegido para ser traslado. Toda vez que el cambio de sitio o recinto no afecta la naturaleza de los
                        servicios contratados, no genera mayores gastos, disminución de ingresos, condiciones ambientales adversas y/o mayor
                        relación de subordinación o dependencia.<br><br>
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