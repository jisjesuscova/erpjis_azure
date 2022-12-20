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
                    <td><h3><center>PAPELETA DE VACACIONES</center></h3></td>   
                </tr>
            </thead>
        </table>
        <hr>
        <table class="table" style="width:100%;">
            <tbody>
                <tr>
                    <td style="text-align: justify;">
                        <font style="font-size: 12px;">
                            <strong>Nombre Completo:</strong> {{ $full_name }}. <strong>RUT:</strong> {{ $rut }}.<br><br>
                            <strong>Fecha de Ingreso:</strong> {{ $entrance_company }}. <strong>Total Feriados Legal:</strong> {{ $legal }}. <strong>Dias Tomados:</strong> {{ $took }}. <strong>Saldo Feriado Legal:</strong> {{ $balance }}.
                            
                            <br><br><br><br>
                        </font>
                        <table style="width:100%;">
                            <tr>
                                <th><center>Desde</center></th>
                                <th><center>Hasta</center></th>
                                <th><center>Días</center></th>
                            </tr>
                            @php($i = 1)
                            @foreach($vacations as $vacation)
                                @php($since = date("d-m-Y", strtotime($vacation->since)))
                                @php($until = date("d-m-Y", strtotime($vacation->until)))
                                @if($i % 2 != 0)
                                    <tr style="background-color:#CCC;">
                                        <td><center>{{ $since }}</center></td>
                                        <td><center>{{ $until }}</center></td>
                                        <td><center>{{ $vacation->days - $vacation->no_valid_days }}</center></td>
                                    </tr>
                                @else
                                    <tr>
                                        <td><center>{{ $since }}</center></td>
                                        <td><center>{{ $until }}</center></td>
                                        <td><center>{{ $vacation->days - $vacation->no_valid_days }}</center></td>
                                    </tr>
                                @endif
                                @php($i = $i + 1)
                            @endforeach
                        </table>
                        <br><br><br><br><br><br>

                        <center><img style="width: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____________________</center>
                        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
                        <center>10.033.741-K&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}&nbsp;&nbsp;</center>
                    </td>
                </tr>
            </tbody>
        </table>
     </body>
</html>