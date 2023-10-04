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
                    <td style="width: 40%;">
                        <img style="width: 60px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/logo.png'))) }}"> 
                    </td>
                    <td>
                        <strong>
                            Liquidación de Sueldo
                        </strong>
                    </td>
                </tr>
            </thead>
        </table>
        <table style="width: 100%;">
            <tbody>
                <tr style="font-size: 12px;">
                    <td style="width: 16.66%;"><strong>Empresa:</strong></td>
                    <td style="width: 33.32%;">{{ $company_name }}</td>
                    <td style="width: 16.66%;">&nbsp;</td>
                    <td style="width: 33.32%;">&nbsp;</td>
                </tr>
                <tr style="font-size: 12px;">
                    <td style="width: 16.66%;"><strong>R.U.T:</strong></td>
                    <td style="width: 33.32%;">{{ $company_rut }}</td>
                    <td style="width: 16.66%;"><strong>Periodo:</strong></td>
                    <td style="width: 33.32%;">{{ $period }}</td>
                </tr>
                <tr style="font-size: 12px;">
                    <td style="width: 16.66%;"><strong>Dirección:</strong></td>
                    <td style="width: 33.32%;">{{ $company_address }}</td>
                    <td style="width: 16.66%;">&nbsp;</td>
                    <td style="width: 33.32%;">&nbsp;</td>
                </tr>
            </tbody>
        </table>
        <table width="100%; padding-top:5px;">
            <tbody>
                <tr style="font-size: 16px;">
                    <td width="100%"><strong><center>Información del Trabajador</center></strong></td>
                </tr>
            </tbody>
        </table>
        <table width="100%; padding-top:5px;">
            <tbody>
                <tr style="font-size: 16px;">
                    <td width="100%"><hr></td>
                </tr>
            </tbody>
        </table>
        <table style="width: 100%; padding-top:5px;">
            <tbody>
                <tr style="font-size: 12px;">
                    <td style="width: 16.66%;"><strong>Nombre:</strong></td>
                    <td style="width: 33.32%;">{{ $employee_full_name }}</td>
                    <td style="width: 16.66%;"><strong>Fecha Ingreso:</strong></td>
                    <td style="width: 33.32%;">{{ $entrance_company }}</td>
                </tr>
                <tr style="font-size: 12px;">
                    <td style="width: 16.66%;"><strong>R.U.T</strong></td>
                    <td style="width: 33.32%;">{{ $employee_rut }}</td>
                    <td style="width: 16.66%;"><strong>Correo:</strong></td>
                    <td style="width: 33.32%;">{{ $company_email }}</td>
                </tr>
                <tr style="font-size: 12px;">
                    <td style="width: 16.66%;"><strong>Cargo:</strong></td>
                    <td style="width: 33.32%;">{{ $job_position }}</td>
                    <td style="width: 16.66%;"><strong>Contrato:</strong></td>
                    <td style="width: 33.32%;">{{ $contract_type }}</td>
                </tr>
                <tr style="font-size: 12px;">
                    <td style="width: 16.66%;"><strong>Sucursal:</strong></td>
                    <td style="width: 33.32%;">{{ $branch_office }}</td>
                    <td style="width: 16.66%;"></td>
                    <td style="width: 33.32%;"></td>
                </tr>
            </tbody>
        </table>
        
        <table style="width: 100%; padding-top:10px;">
            <tbody>
                <tr style="font-size: 14px; margin-top:10px;">
                    <td colspan="6"><hr></td>
                </tr>
                <tr style="font-size: 12px; margin-top:10px;">
                    <td colspan="3"><strong><center>INDICADORES</center></strong></td>
                    <td colspan="3"><strong><center>APORTE EMPRESA</center></strong></td>
                </tr>
                <tr style="font-size: 14px; margin-top:10px;">
                    <td colspan="6"><hr></td>
                </tr>
                <tr style="font-size: 12px;">
                    <td style="width: 16.66%;"><strong>Días Trab:</strong> {{ $work_days }}</td>
                    <td style="width: 16.66%;"><strong>Ausencia:</strong> {{ $absence_days }}</td>
                    <td style="width: 16.66%;"><strong>Días Lic:</strong> {{ $license_days }}</td>
                    <td style="width: 16.66%;"></td>
                    <td style="width: 16.66%;"></td>
                    <td style="width: 16.66%;"></td>
                </tr>
                <tr style="font-size: 12px;">
                    <td style="width: 16.66%;"><strong>S.Base:</strong> {{ $base_salary }}</td>
                    <td style="width: 16.66%;"><strong>AFP:</strong> {{ $pention }}</td>
                    <td style="width: 16.66%;"><strong>Salud:</strong> {{ $health }}</td>
                    <td style="width: 16.66%;"><strong>Mutual:</strong> {{ $mutual_name }}</td>
                    <td style="width: 16.66%;"><strong>Mutual $:</strong> $ {{ $mutual_amount }}</td>
                    <td style="width: 16.66%;"><strong>Seg Sis:</strong> $ {{ $employer_insurance }}</td>
                </tr>
                <tr style="font-size: 12px;">
                    <td style="width: 16.66%;"><strong>Tasa AFP:</strong> {{ $pention_value }}%</td>
                    <td style="width: 16.66%;"><strong>P. Salud:</strong> {{ $health_payment_value }}</td>
                    <td style="width: 16.66%;"></td>
                    <td style="width: 16.66%;"><strong>CCAF:</strong> {{ $compentation_cashier }}</td>
                    <td style="width: 16.66%;"><strong>Sis:</strong> {{ $sis_value }}%</td>
                    <td style="width: 16.66%;"><strong>Metlife:</strong> $ {{ $health_employer_insurance }}</td>
                </tr>
                <tr style="font-size: 12px;">
                    <td style="width: 16.66%;"><strong>UTM:</strong> $ {{ $utm }}</td>
                    <td style="width: 16.66%;"><strong>UF: </strong> $ {{ $uf }}</td>
                    <td style="width: 16.66%;"><strong>Cargas:</strong> {{ $family_group }}</td>
                    <td style="width: 16.66%;"><strong>S. Cesan:</strong> $ {{ $seg_cesan_emp }}</td>
                    <td style="width: 16.66%;"></td>
                    <td style="width: 16.66%;"></td>
                </tr>
            </tbody>
        </table>
        <table style="width: 100%; padding-top:5px;">
            <tbody>
                <tr style="font-size: 14px; margin-top:10px;">
                    <td colspan="4"><hr></td>
                </tr>
                <tr style="font-size: 12px; margin-top:10px;">
                    <td colspan="2"><strong><center>HABERES</center></strong></td>
                    <td colspan="2"><strong><center>DESCUENTOS</center></strong></td>
                </tr>
                <tr style="font-size: 14px; margin-top:10px;">
                    <td colspan="4"><hr></td>
                </tr>
                @if(!isset($positive_values['names'])) 
                    @php($items =0)
                @else
                    @if($positive_values['names'] > $negative_values['names']) @php($items = count($positive_values['names'])) @else @php($items = count($negative_values['names'])) @endif
                @endif
                @for($i = 0; $i < $items; $i++)
                    <tr style="font-size: 12px;">
                        @if(isset($positive_values['names'][$i]))
                            @if($positive_values['amounts'][$i] != 0)
                                @if($positive_values['totalization'][$i] == 1) 
                                    <td style="width: 33.32%;"><strong>{{ $positive_values['names'][$i] }}:</strong></td>
                                    <td style="width: 16.66%;"><strong>$ {{ $positive_values['amounts'][$i] }}</strong></td>
                                @else
                                    <td style="width: 33.32%;">{{ $positive_values['names'][$i] }}:</td>
                                    <td style="width: 16.66%;">$ {{ $positive_values['amounts'][$i] }}</td>
                                @endif
                            @endif
                        @else
                            <td style="width: 33.32%;"></td>
                            <td style="width: 16.66%;"></td>
                        @endif
                        @if(isset($negative_values['names'][$i]))
                            @if($negative_values['amounts'][$i] != 0)
                                @if($negative_values['totalization'][$i] == 1) 
                                    <td style="width: 33.32%;"><strong>{{ $negative_values['names'][$i] }}:</strong></td>
                                    <td style="width: 16.66%;"><strong>$ {{ $negative_values['amounts'][$i] }}</strong></td>
                                @else
                                    <td style="width: 33.32%;">{{ $negative_values['names'][$i] }}:</td>
                                    <td style="width: 16.66%;">$ {{ $negative_values['amounts'][$i] }}</td>
                                @endif
                            @endif
                        @endif
                    </tr>
                @endfor
                <tr style="font-size: 14px; margin-top:10px;">
                    <td colspan="4"><hr></td>
                </tr>
                <tr style="font-size: 12px;">
                    <td style="width: 33.32%;"><strong>Total Haberes:</strong></td>
                    <td style="width: 16.66%;"><strong>$ {{ $total_assets }}</strong></td>
                    <td style="width: 33.32%;"><strong>Total Descuentos:</strong></td>
                    <td style="width: 16.66%;"><strong>$ {{ $total_discounts }}</strong></td>
                </tr>
                <tr style="font-size: 14px; margin-top:10px;">
                    <td colspan="4"><hr></td>
                </tr>
            </tbody>
        </table>
        <table style="width: 100%; padding-top:5px;">
            <tbody>
                <tr style="font-size: 14px; margin-top:10px; text-align: justify;">
                    <td style="width: 50%;">
                    </td>
                    <td style="width: 50%; text-align: right;">
                        <strong>Total a Pagar $ {{ $liquid_salary }}.-
                    </td>
                </tr>
            </tbody>
        </table>
        <table style="width: 100%; padding-top:5px;">
            <tbody>
                <tr style="font-size: 10px; margin-top:10px; text-align: justify;">
                    <td style="width: 100%;">
                        Certifico haber recibido en este acto a mi entera satisfacción, el
                        total de <strong>{{ $liquid_salary_words }}</strong>. Asimismo, declaro que
                        nada se me adeuda y no tener reclamo alguno en contra de la
                        empresa J I S PARKING SPA por concepto de remuneraciones.
                    </td>
                </tr>
            </tbody>
        </table>
        <br><br>

        <center>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img style="width: 120px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;<img style="width: 400px;" src="{{ $image }}" class="card-img-top img-responsive" alt="Card"></center>
        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
        <center>10.033.741-K&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}&nbsp;&nbsp;</center>
        
    </body>
</html>