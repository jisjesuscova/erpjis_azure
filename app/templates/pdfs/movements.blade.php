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
                    <img src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/logo.png'))) }}"> 
                </tr>
            </thead>
        </table>
        <table class="table table-bordered" style="width:100%;">
            <thead>
                <tr>
                    <td><h6><b>Fecha:</b> {{ $date }}</h6></td>   
                </tr>
            </thead>
        </table>
        <table class="table table-bordered" style="width:100%;">
            <thead>
                <tr>
                    <td><h2><font style="font-family:arial;"><center>Guía de Salida</center></font></h2></td>   
                </tr>
            </thead>
        </table>
        <hr>
        <table class="table table-bordered" style="width:100%;">
            <thead>
                <tr>
                    <td>
                        <h5>
                            <center>
                                Código
                            </center>
                        </h5>
                    </td>
                    <td>
                        <h5>
                            <center>
                                Descripción
                            </center>
                        </h5>
                    </td>
                    <td>
                        <h5>
                            <center>
                                Uni
                            </center>
                        </h5>
                    </td>
                    <td>
                        <h5>
                            <center>
                                P. Unitario
                            </center>
                        </h5>
                    </td>
                    <td>
                        <h5>
                            <center>
                                Valor Total
                            </center>
                        </h5>
                    </td>
                </tr>
            </thead>
            <tbody>
                @foreach($movements_products as $movement_product)
                    <tr>
                        <td>
                            <center>
                                {{ $movement_product->code }}
                            </center>
                        </td>
                        <td>
                            <center>
                                {{ $movement_product->description }}
                            </center>
                        </td>
                        <td>
                            <center>
                                @php($qty = $movement_product->quantity*-1)
                                {{ $qty }}
                            </center>
                        </td>
                        <td>
                            <center>
                                {{ $movement_product->cost }}
                            </center>
                        </td>
                        <td>
                            <center>
                                {{ $qty*$movement_product->cost }}
                            </center>
                        </td>
                    </tr>
                @endforeach
            </tbody>
        </table>
     </body>
</html>