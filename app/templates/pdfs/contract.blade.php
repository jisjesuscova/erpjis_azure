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
    <body style="width:100%; font-size: 12px;">
        <table class="table table-bordered" style="width:100%; font-family: Arial, Helvetica, sans-serif;">
            <thead>
                <tr>
                    <img style="width: 80px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/logo.png'))) }}"> 
                </tr>
            </thead>
        </table>
        <table class="table table-bordered" style="width:100%; font-family: Arial, Helvetica, sans-serif;">
            <thead>
                <tr>
                    <td><h3><center> CONTRATO INDIVIDUAL DE TRABAJO</center></h3></td>   
                </tr>
            </thead>
        </table>
        <hr>
        <table class="table" style="width:100%;">
            <tbody>
                <tr>
                    <td style="text-align: justify; font-family: Arial, Helvetica, sans-serif;">
                        En Estación Central, Santiago, <strong>{{ $entrance_company }}</strong>, entre <strong>JIS Parking SPA.</strong>, sociedad del giro 
                        administración de estacionamientos y parquímetros, Rol Único Tributario <strong>76063822-6</strong>, representada por don 
                        <strong>MARCELO ALEJANDRO INZUNZA GONZÁLEZ</strong> cédula de identidad número  <strong>10.033.741-K</strong>, en adelante “EMPLEADOR”, 
                        ambos con domicilio en <strong>Matucana número 40</strong>, comuna de <strong>Estación Central</strong> y ciudad <strong>Santiago</strong>, 
                        y Sr(a) <strong>{{ $full_name }}</strong>, cédula nacional de identidad número <strong>{{ $rut }}</strong>, con domicilio en 
                        <strong>{{ $employee_address }}</strong>, perteneciente a la comuna de <strong>{{ $commune }}</strong>, de estado civil 
                        <strong>{{ $civil_state }}</strong>, en adelante “TRABAJADOR”, se conviene el siguiente contrato individual de trabajo,
                        que se rige por el Código del Trabajo, sus modificaciones y estipulaciones que se expresan a continuación:<br><br>
                        <strong>PRIMERO:</strong> El EMPLEADOR contrata a Sr(a) <strong>{{ $full_name }}</strong>, para realizar las labores, funciones y trabajos
                        de <strong>{{ $position }}</strong>, de la sociedad señalada, y todas las actividades relacionadas directa o indirectamente con este
                        tipo de cargo, las que realizará en dependencias del empleador. Su labor la desarrollará en la sucursal del EMPLEADOR
                        denominada: <strong>{{ $branch_office_name }}</strong> ubicada en <strong>{{ $branch_office_address }}</strong>. El lugar para desempeñar sus
                        funciones podrá mutar consensuadamente por las partes, lo que deberá constar en respectivo anexo de contrato de trabajo.<br><br>
                        <strong>SEGUNDO:</strong> El TRABAJADOR se obliga a ejecutar los trabajos concernientes a su empleo en la forma más eficaz posible,
                        empleando en ello la mayor responsabilidad, eficacia y dedicación. Entre las funciones que deberá efectuar el TRABAJADOR,
                        se destacan:<br><br>
                        • {{ $job_position_functions }}<br><br>
                        Será responsabilidad del trabajador el aseo, limpieza y mantención de su lugar de trabajo.<br><br>
                        <strong>TERCERO:</strong> Las partes dejan expreso testimonio que en atención a la naturaleza de las labores convenidas y a las
                        necesidades que satisfacen las funciones de la Empresa y al hecho que se ejecutan en un establecimiento de comercio que
                        atiende directamente al público, de conformidad con lo dispuesto en la legislación laboral vigente, reconocen y aceptan que el
                        TRABAJADOR, en cumplimiento de su jornada semanal, estará exceptuado del descanso dominical, teniendo derecho a un
                        mínimo de un día de descanso a la semana, en compensación de las actividades que desarrolle en domingo. El (los) día (s) de
                        descanso, le será (n) otorgado (s) al TRABAJADOR mediante un sistema de turnos, de acuerdo con la planificación establecida
                        y las necesidades de la Empresa, día o días de descanso que dependerán de si la semana de trabajo se ha distribuido en cinco
                        o seis días consecutivos de labor.<br><br>
                        @if($full_time_id == 1)
                            El TRABAJADOR se obliga a cumplir una jornada máxima de 45 horas semanales, que se distribuirá en cinco días de trabajo,
                            por dos de descanso en cada semana; o bien, en seis días consecutivos de trabajo, por uno de descanso, según lo determine
                            el EMPLEADOR conforme al sistema de turnos ya mencionado.
                            Los días de trabajo incluirán, en cualquier caso, los domingos
                            y festivos, por tratarse de labores que exigen desarrollarse en continuidad por las necesidades que satisfacen, las que están
                            exentas del descanso dominical. El empleador podrá efectuar las correspondientes adecuaciones en la distribución de la jornada de trabajo, en las cuales el
                            trabajador consiente expresamente, para los efectos de dar cumplimiento a lo dispuesto por el inciso cuarto del artículo 38
                            contenido en el Código del Trabajo.<br><br>
                        @endif
                        Queda expresamente convenido por las partes que dicha jornada semanal será cumplida por el TRABAJADOR mediante un
                        sistema de turnos que le asigne el EMPLEADOR, cuyas diversas y diferentes modalidades se especifican en documento
                        anexo denominado <strong>"{{ $time }}"</strong> el cual, suscrito también por las partes, forma parte integrante del
                        presente instrumento y del contrato de trabajo, recibiendo el trabajador copia de ambos.
                        La empresa comunicará al TRABAJADOR, por medio de un anuncio publicado en su lugar de trabajo, o por cualquier otra vía
                        idónea, con a lo menos 7 días de anticipación, el turno en el cual éste deberá laborar cada semana. En todo caso, la Empresa
                        se reserva expresamente el derecho de alterar la distribución de la jornada de trabajo, de conformidad a la Ley, estableciendo
                        otros esquemas de turnos.<br><br>
                        Se prohíbe expresamente al TRABAJADOR ejecutar labores en horas extraordinarias, si ellas no han sido convenidas por
                        escrito con el empleador o quien haga sus veces. Queda, asimismo, expresa y estrictamente prohibido al TRABAJADOR
                        permanecer en el lugar de trabajo, fuera de su jornada ordinaria, sin contar con la autorización escrita del empleador. Para
                        estos efectos, se acuerda que, cuando las circunstancias lo justifiquen, el TRABAJADOR podrá trabajar horas extraordinarias,
                        previo acuerdo entre las partes.<br><br>
                        
                        @if($full_time_id == 0)
                            La jornada diaria de labor se suspenderá por un período para colación, periodo que no podrá ser inferior a 30 minutos, no
                            formará parte de la jornada de trabajo ni se computará para determinar su extensión. El descanso indicado también se otorgará
                            mediante sistema de turnos, con el objeto de no paralizar las actividades de la sucursal.<br><br><br><br>
                        @endif
                        <br><br><br><br><center><font style="font-size: 10px;">1 de 11</font></center>
                        <div class="page-break"></div>
                        
                        @if($full_time_id == 1)
                            La jornada diaria de labor se suspenderá por un período para colación, periodo que no podrá ser inferior a 30 minutos, no
                            formará parte de la jornada de trabajo ni se computará para determinar su extensión. El descanso indicado también se otorgará
                            mediante sistema de turnos, con el objeto de no paralizar las actividades de la sucursal.<br><br>
                        @endif
                        Es acuerdo de los contratantes que, por regla general, el descanso compensatorio de los días festivos que labore, le será
                        otorgado al en un día domingo dentro del mismo mes calendario en que haya trabajado el festivo, o en otro mes distinto, dentro
                        del mismo año calendario, pudiendo contabilizarse este día para los efectos del cumplimiento de lo dispuesto en el artículo 38,
                        inciso cuarto, del Código del Trabajo.<br><br>
                        Si no se otorgare descanso compensatorio, en la forma antes mencionada o en cualquier otra que la ley permita, la
                        remuneración de las horas laboradas en días festivos se pagará al trabajador con el recargo que la ley establece para las horas
                        extraordinarias.<br><br>
                        <strong>CUARTO:</strong> El trabajador recibirá a título de remuneración un sueldo base bruto mensual de $ <strong>{{ $salary }}.-</strong> por las labores indicadas
                        en la cláusula segunda del presente contrato.
                        Además, el empleador el empleador opta, en relación con este beneficio, por la alternativa contemplada en el artículo 50 del
                        Código del Trabajo, vale decir, por abonar o pagar el 25% de lo devengado en el respectivo ejercicio comercial por concepto de
                        remuneraciones mensuales, con un tope máximo de 4,75 ingresos mínimos mensuales. A la suma que legalmente pudiere
                        corresponder por concepto de este beneficio, en el evento de existir utilidades líquidas que hicieran exigible el pago de
                        gratificación legal, se imputará lo pagado en razón de la gratificación convencional que se pacta a continuación. Vale decir,
                        ambas gratificaciones no se sumarán en caso alguno y aquello que se hubiere pagado por concepto de gratificación
                        convencional, por estar contractualmente garantizada, eximirá al empleador del pago de lo que pudiere corresponder por
                        gratificación legal.<br><br>
                        Por otra parte, se pacta una gratificación garantizada, haya o no utilidades, ascendente al 25% de lo devengado por el
                        trabajador en el respectivo ejercicio comercial por concepto de remuneración, con el tope máximo legal que proceda, el cual en
                        ningún caso podrá exceder del equivalente a 4,75 ingresos mínimos al año. Esta gratificación se pagará mensualmente, en la
                        misma oportunidad establecida para el pago del sueldo.<br><br>
                        El pago de la gratificación en la forma que antecede exime al empleador de la obligación de gratificar al trabajador en
                        conformidad a las normas del artículo 46 y siguientes del Código del Trabajo en el evento que la empresa obtenga utilidades en
                        los términos allí señalados.<br><br>
                        Estas remuneraciones se pagarán por mensualidades vencidas, mediante transferencia bancaria o mediante cheque a su
                        orden dentro de los cinco días hábiles del mes siguiente al que corresponda cada pago.<br><br>
                        <strong>QUINTO:</strong> Son obligaciones del TRABAJADOR:<br><br>
                        • Cumplir la jornada de trabajo en su totalidad diaria, según lo señalado precedentemente.<br><br>
                        • Justificar a su jefe directo las inasistencias por enfermedad, mediante certificado otorgado de conformidad a la legislación
                        vigente.<br><br>
                        • Asumir las responsabilidades propias del trabajo para el que es contratado y ejercerlo conforme a las prácticas normales de
                        este tipo de trabajo y cumplir fielmente con las instrucciones que para el ejercicio de su trabajo y labores le señale la gerencia o
                        su jefe directo.<br><br>
                        • Firmar el libro de asistencia o reloj control a la entrada y a la salida del trabajo. Se presumirá la ausencia del TRABAJADOR
                        por la sola concurrencia de no cumplir con esta obligación.<br><br>
                        • Ejecutar sus labores con prontitud y eficacia, de acuerdo a las instrucciones y normas laborales que se le impartan, evitando
                        comprometer la seguridad y salud propia y del resto de trabajadores de la empresa.<br><br>
                        • Respetar las normas contenidas en el Reglamento Interno de Orden Higiene y Seguridad, las que declara conocer;
                        reglamento que recibe en este acto.<br><br>
                        • Cuidar y mantener en perfecto estado de conservación los útiles, herramientas e implementos necesarios para su trabajo.<br><br>
                        <strong>SEXTO:</strong> Queda prohibido al TRABAJADOR:<br><br>
                        • Dar a terceras personas informaciones estimadas como confidenciales por la empresa.<br><br>
                        @if($full_time_id == 0)
                            <br><br><br><br>
                        @endif
                        
                        <br><br><br><br><br><center><font style="font-size: 10px;">2 de 11</font></center>

                        <div class="page-break"></div>
                        • Firmar o marcar registro de asistencia de horarios de otro trabajador de la empresa. El trabajador que fuere sorprendido
                        firmando o marcando el registro de asistencia de otro trabajador, será considerado como autor de falta grave a las obligaciones
                        del contrato.<br><br>
                        • Realizar o ejecutar durante la jornada de trabajo cualquier labor ajena a las de la empresa.<br><br>
                        <strong>SÉPTIMO:</strong> El presente contrato de trabajo terminará sin derecho a indemnización, cuando el trabajador incurra en alguna
                        FALTA GRAVE, de acuerdo a lo establecido en el artículo. 160 numeral 7 del Código del Trabajo, por lo que las partes
                        consideran como tales, las faltas que más adelante se detallan, entre otras cosas:<br><br>
                        • Presentarse al trabajo en estado de ebriedad, introducir o beber bebidas alcohólicas en el recinto de la empresa, durante su
                        jornada de trabajo.<br><br>
                        • Efectuar negociaciones con los bienes, productos o servicios que venda la empresa, o de terceros.<br><br>
                        • No otorgar boleta o guía en toda venta, cobro de estacionamiento, otorgarlas sin complementar toda la información que
                        dichos documentos requieran, otorgarlas por menos valor o mayor valor a la venta efectiva de acuerdo a las disposiciones de
                        D.L. 825 de reglamento y, Código Tributario, especialmente en el Art. 97 Nº 10.<br><br>
                        • Recibir dos o más reclamos por escrito de clientes que traten de engaño, fraude o mal trato de palabras o de hechos. • Hacer
                        abandono de su puesto de trabajo sin causa justificada.<br><br>
                        • Registrar 3 o más diferencias de valores, en el mes en el resumen diario de ventas o recaudación.<br><br>
                        • Ocultar atrasos o inasistencias propias o de terceros en el correspondiente libro de asistencias.<br><br>
                        • El trabajador es responsable en caso de pérdida del libro de asistencia, pues se encuentra a su cargo.<br><br>
                        • Efectuar cambios de cheques, por dinero efectivo.<br><br>
                        • Permitir el estacionamiento de vehículos de cualquier tipo sin pagar dentro del recinto de estación de servicio sin haber sido
                        autorizado por su jefatura.<br><br>
                        • No cuidar debidamente su aseo personal, de la ropa de trabajo y presentación personal.<br><br>
                        • Promover o provocar juegos de azar, riñas o alteraciones de cualquier especie con sus compañeros o jefes durante la jornada
                        de trabajo en el establecimiento.<br><br>
                        • Negarse a acatar las órdenes e instrucciones que reciba de sus jefes, a los cuales deberá especialmente lealtad y respeto,
                        debiendo guardar la más absoluta reserva de todas las operaciones de su empleador o sus clientes.<br><br>
                        Producido cualquiera de estos hechos, el presente Contrato de Trabajo expirará de inmediato y sin derecho a indemnización
                        alguna.<br><br>

                        <strong>OCTAVO:</strong> Las partes acuerdan expresamente elevar todas las cláusulas estipuladas en este contrato a la calidad de esencial.
                        A su vez, convienen que la sola inobservancia de las cláusulas conformantes del presente instrumento, constituye
                        incumplimiento grave a las obligaciones, configurándose la causal establecida en el artículo 160 numeral 7 del Código del
                        Trabajo.<br><br>
                        <strong>NOVENO:</strong> El plazo de duración de este contrato tiene carácter de plazo fijo con un primer vencimiento a contar del día y hasta
                        <strong>{{ $first_extention_date }}</strong> . Transcurrido dicho plazo el contrato se entenderá renovado automáticamente hasta <strong>{{ $second_extention_date }}</strong> . Sino hubiera comunicación escrita de la empleadora en sentido contrario, vencido el plazo de esta primera prorroga,
                        sin que la empleadora haya notificado por escrito al trabajador su intención de no perseverar en el contrato, se entenderá que
                        este tiene duración INDEFINIDA.<br><br>
                        Sin perjuicio de lo anterior, se le podrá poner término al contrato de trabajo con ocasión a la ocurrencia de alguna de las otras
                        causales establecidas en disposiciones legales vigentes.<br><br>
                        <strong>DÉCIMO:</strong> El TRABAJADOR señala que, para efectos de previsión y seguridad social, está afiliado a la AFP: <strong>{{ $pention }}</strong>, y a la
                        institución de salud previsional: <strong>{{ $health }}</strong>. Asimismo, declara que asume su propia responsabilidad por cambios o modificaciones
                        que realice con su situación previsional; de forma tal que, el EMPLEADOR sólo se obliga en esta materia a enterar
                        oportunamente las respectivas imposiciones en régimen de salud y previsión a las instituciones en las que se encuentre
                        afiliado, según su propia declaración.
                        
                        <br><br><br><br><center><font style="font-size: 10px;">3 de 11</font></center>
                        <div class="page-break"></div>

                        <strong>UNDÉCIMO:</strong> Se deja constancia que el trabajador ingresó al servicio del EMPLEADOR con fecha <strong>{{ $entrance_company }}</strong> .<br><br>
                        <strong>DUODÉCIMO:</strong> Para todos los efectos legales, las partes fijan domicilio en Santiago, sometiéndose a la Jurisdicción de sus
                        Tribunales.<br><br>
                        <strong>DÉCIMO TERCERO:</strong> Para constancia el presente contrato se firma en tres ejemplares, declarando el TRABAJADOR haber
                        leído y recibido en este acto un ejemplar de dicho instrumento, que es el fiel reflejo de la relación laboral convenida.
                        <br><br><br><br><br><br><br><br>
                        <center><img style="width: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____________________</center>
                        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
                        <center>76.063.822-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}</center>
                        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><center><font style="font-size: 10px;">4 de 11</font></center>
                        <div class="page-break"></div>

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
                                    <td><h3><center> ANEXO TURNOS JORNADA</center></h3></td>   
                                </tr>
                            </thead>
                        </table>
                        <hr>
                        <table class="table" style="width:100%;">
                            <tbody>
                                <tr>
                                    <td style="text-align: justify;">
                                        <strong>PRIMERO:</strong> Conforme lo dispuesto por el artículo 22 del Código del Trabajo, a partir del <strong>{{ $entrance_company }}</strong>, el
                                        TRABAJADOR se obliga a ejecutar sus labores en jornada semanal ordinaria de 45 horas, distribuidas de lunes a domingo, con
                                        1 o 2 días de descanso a la semana, según corresponda, en razón de encontrarse en el caso previsto por el artículo 38
                                        numerales 2 o 7 del Código del Trabajo, de acuerdo a las distribuciones semanales que a continuación se señalan, y cuya
                                        programación mensual le será informada a más tardar durante la última semana del mes anterior al del inicio de la nueva
                                        programación:<br><br>
                                        <strong>Condiciones de Turnos de Trabajo:</strong><br>
                                        <center><img style="width:800px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/schedule.jpg'))) }}"><br></center>
                                        Duración de la jornada diaria Tiempo Completo: La jornada diaria tendrá una duración de entre 7 hasta 8,20 horas, sin
                                        considerar para estos efectos el tiempo destinado a colación.
                                        Duración de la jornada diaria Medio Tiempo: La jornada diaria tendrá una duración de entre 4, 5 y 10 horas, sin considerar para
                                        estos efectos el tiempo destinado a colación.<br><br>
                                        <strong>SEGUNDO:</strong> El presente anexo de contrato individual de trabajo, que pasa a ser parte integrante del contrato de trabajo vigente
                                        entre las partes, se firma en tres ejemplares del mismo tenor, dejando expresa constancia que en este acto el trabajador recibe
                                        uno de ellos a su entera satisfacción, declarando, además, haberlo leído dando su conformidad a todas y cada una de las
                                        estipulaciones contenidas en él.<br><br><br><br><br><br>
                                        <center><img style="width: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____________________</center>
                                        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
                                        <center>76.063.822-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}&nbsp;&nbsp;</center>
                                        <br><br><br><br><br><center><font style="font-size: 10px;">5 de 11</font></center>
                                    </td>
                                </tr>
                            </tbody>
                        </table>

                        <div class="page-break"></div>

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
                                    <td><h3><center>ANEXO AL CONTRATO INDIVIDUAL DE TRABAJO</center></h3></td>   
                                </tr>
                            </thead>
                        </table>
                        <hr>
                        <table class="table" style="width:100%;">
                            <tbody>
                                <tr>
                                    <td style="text-align: justify;">
                                        En Estación Central, Santiago, a <strong>{{ $entrance_company }}</strong>, entre <strong>JIS PARKING SPA.</strong>, Rol Único Tributario número <strong>76063822-6</strong>,
                                        representada legalmente por don <strong>MARCELO ALEJANDRO INZUNZA GONZÁLEZ</strong>, cédula nacional de identidad número
                                        <strong>10.033.741-K</strong>, en adelante “EMPLEADOR”, y Sr(a) <strong>{{ $full_name }}</strong>, cédula nacional de identidad número
                                        <strong>{{ $rut }}</strong>, en adelante “TRABAJADOR”, se ha convenido el siguiente anexo de contrato, cuyas cláusulas señalan:<br><br>
                                        <strong>PRIMERO:</strong> El TRABAJADOR, para efectos de recepción de notificaciones de asistencia, indica el correo electrónico:<br><br>
                                        <strong>{{ $company_email }}</strong>.<br><br>
                                        <strong>SEGUNDO:</strong> El TRABAJADOR autoriza se envíen a la casilla electrónica señalada en la cláusula precedente, todas las
                                        notificaciones de asistencia realizadas por este, las que se materializan por un ticket de marcación enviadas electrónicamente.<br>
                                        <strong>TERCERO:</strong> Las notificaciones de asistencia serán enviadas cada vez que el TRABAJADOR realice un registro de asistencia.<br>
                                        <strong>CUARTO:</strong> El TRABAJADOR podrá modificar unilateralmente la casilla electrónica señalada en la cláusula primera de este
                                        anexo de contrato. Para este efecto, deberá comunicárselo al departamento de Recursos Humanos o realizar el cambio por
                                        intermedio del sitio “Relojcontrol.com” sección “Portal del Trabajador”.<br>
                                        <strong>QUINTO:</strong> En caso que el TRABAJADOR no reciba en la casilla electrónica indicada en la cláusula primera del presente anexo,
                                        deberá comunicar dicha situación al departamento de Recursos Humanos a fin que se le entregue copia de la notificación en
                                        cuestión.<br>
                                        <strong>SEXTO:</strong> En todo lo demás, se mantienen íntegramente vigente las estipulaciones del contrato individual de trabajo.<br>
                                        <strong>SÉPTIMO:</strong> El presente anexo de contrato individual de trabajo, que pasa a ser parte integrante del contrato de trabajo vigente
                                        entre las partes, se firma en tres ejemplares del mismo tenor, dejando expresa constancia que en este acto el trabajador recibe
                                        uno de ellos a su entera satisfacción, declarando, además, haberlo leído dando su conformidad a todas y cada una de las
                                        estipulaciones contenidas en él.<br><br><br><br><br><br>
                                        <center><img style="width: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____________________</center>
                                        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
                                        <center>76.063.822-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}&nbsp;&nbsp;</center>
                                        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><center><font style="font-size: 10px;">6 de 11</font></center>
                                    </td>
                                </tr>
                            </tbody>
                        </table>

                        <div class="page-break"></div>

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
                                    <td><h3><center>CONTROL DE ENTREGA, TOMA DE CONOCIMIENTO Y ACUSO DE RECIBO DEL DERECHO A SABER U OBLIGACIÓN A INFORMAR </center></h3></td>   
                                </tr>
                            </thead>
                        </table>
                        <hr>
                        <table class="table" style="width:100%;">
                            <tbody>
                                <tr>
                                    <td style="text-align: justify;">
                                        Se deja expresa constancia, de acuerdo a lo establecido en el D.S. N° 40 que, he recibido en forma gratuita un ejemplar del Derecho a Saber u Obligación a Informar por
                                        parte de la empresa JIS PARKING SPA. El cual se busca informar los riesgos a los cuales se encontrará expuesto en el desarrollo de sus labores de {{ $position }}, en nuestras diversas sucursales.<br><br>
                                        Así también declaro bajo mi firma, haber recibido, leído y comprendido el presente documento, del cual doy fé de conocer el contenido de éste y me hago responsable de su estricto cumplimiento en cada uno de sus artículos, no puediendo alegar desconocimiento de su texto a contar de la fecha {{ $entrance_company }}.
                                        <br><br><br><br><br><br>
                                        <center><img style="width: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____________________</center>
                                        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
                                        <center>76.063.822-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}&nbsp;&nbsp;</center>
                                        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><center><font style="font-size: 10px;">7 de 11</font></center>
                                    </td>
                                </tr>
                            </tbody>
                        </table>

                        <div class="page-break"></div>

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
                                    <td><h3><center>CONTROL DE ENTREGA, TOMA DE CONOCIMIENTO Y ACUSO DE RECIBO DEL REGLAMENTO INTERNO DE ORDEN, HIGIENE Y SEGURIDAD </center></h3></td>   
                                </tr>
                            </thead>
                        </table>
                        <hr>
                        <table class="table" style="width:100%;">
                            <tbody>
                                <tr>
                                    <td style="text-align: justify;">
                                        Se deja expresa constancia, de acuerdo a lo establecido en el D.S. N° 40 que, he recibido en forma gratuita un ejemplar del Reglamento Interno de Orden, Higiene y Seguridad por
                                        parte de la empresa JIS PARKING SPA. El cual se busca informar los riesgos a los cuales se encontrará expuesto en el desarrollo de sus labores de {{ $position }}, en nuestras diversas sucursales.<br><br>
                                        Así también declaro bajo mi firma, haber recibido, leído y comprendido el presente documento, del cual doy fé de conocer el contenido de éste y me hago responsable de su estricto cumplimiento en cada uno de sus artículos, no puediendo alegar desconocimiento de su texto a contar de la fecha {{ $entrance_company }}.
                                        <br><br><br><br><br><br>
                                        <center><img style="width: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____________________</center>
                                        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
                                        <center>76.063.822-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}&nbsp;&nbsp;</center>
                                        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><center><font style="font-size: 10px;">8 de 11</font></center>
                                    </td>
                                </tr>
                            </tbody>
                        </table>

                        <div class="page-break"></div>

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
                                    <td><h3><center>CONTROL DE ENTREGA, TOMA DE CONOCIMIENTO Y ACUSO DE RECIBO DEL REGLAMENTO INTERNO DE ORDEN, HIGIENE Y SEGURIDAD (RIOHS) Y REGISTRO DE RECEPCION DE OBLIGACION DE INFORMAR (ODI). Instructivo Covid-19</center></h3></td>   
                                </tr>
                            </thead>
                        </table>
                        <hr>
                        <table class="table" style="width:100%;">
                            <tbody>
                                <tr>
                                    <td style="text-align: justify;">
                                        De acuerdo con lo establecido en el D.S. N° 40, que aprueba el reglamento sobre prevención de los riesgos profesionales en su Título VI, Art 21. referido a "las obligaciones de informar de los riesgos laborales" el trabajador <strong>{{ $full_name }}</strong> cédula de identidad <strong>{{ $rut }}</strong> quien desempeña las labores en la empresa como <strong>{{ $position }}</strong>, se encuentra en conocimiento
                                        de los riesgos por exposición laboral a COVID-19 y las medidas que se debe tomar para evitar su contagio.<br><br>
                                        Además, se solicita que se respeten las restantes normas de higiene y seguridad (Principalmente las indicaciones RIOHS) y participe activamente en las actividades de prevención.
                                        <br><br><br><br><br><br>
                                        <center><img style="width: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____________________</center>
                                        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
                                        <center>76.063.822-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}&nbsp;&nbsp;</center>
                                        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><center><font style="font-size: 10px;">9 de 11</font></center>
                                    </td>
                                </tr>
                            </tbody>
                        </table>

                        <div class="page-break"></div>

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
                                    <td><h3><center>ENTREGA DE ELEMENTOS DE PROTECCION PERSONAL</center></h3></td>   
                                </tr>
                            </thead>
                        </table>
                        <hr>
                        <table class="table" style="width:100%;">
                            <tbody>
                                <tr>
                                    <td style="text-align: justify;">
                                        De acuerdo a lo estipulado en la Ley 16.744, Art. 68 inciso tres “Las empresas deberán proporcionar a sus trabajadores, los equipos e implementos de protección necesarios, no pudiendo en caso alguno cobrarles su valor”.<br><br><br><br>
                                        <table class="table" style="width:100%; border: none;">
                                            <tbody>
                                                <tr>
                                                    <td style="text-align: justify;">
                                                        <strong>RUT:</strong> {{ $rut }}
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td style="text-align: justify;">
                                                        <strong>NOMBRE:</strong> {{ $full_name }}
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td style="text-align: justify;">
                                                        <strong>CARGO:</strong> {{ $position }}
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td style="text-align: justify;">
                                                        <strong>SUCURSAL:</strong> {{ $branch_office_name }}
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td style="text-align: justify;">
                                                        <strong>ELEMENTOS:</strong> <br><br>____________________________________________________________________________<br><br>____________________________________________________________________________
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table><br><br>
                                        Todos entregados el día <strong>{{ $entrance_company }}</strong>.
                                        <br><br><br><br><br><br>
                                        <center><img style="width: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____________________</center>
                                        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
                                        <center>76.063.822-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}&nbsp;&nbsp;</center>
                                        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><center><font style="font-size: 10px;">10 de 11</font></center>
                                    </td>
                                </tr>
                            </tbody>
                        </table>

                        <div class="page-break"></div>

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
                                    <td><h3><center>ANEXO DE CONTRATO DE TRABAJO BONO META MENSUAL</center></h3></td>   
                                </tr>
                            </thead>
                        </table>
                        <hr>
                        <table class="table" style="width:100%;">
                            <tbody>
                                <tr>
                                    <td style="text-align: justify;">
                                        En Estación Central, Santiago, a <strong>{{ $entrance_company }}</strong>, entre <strong>JIS PARKING SPA.</strong>, Rol Único Tributario número <strong>76063822-6</strong>,
                                        representada legalmente por don <strong>MARCELO ALEJANDRO INZUNZA GONZÁLEZ</strong>, cédula nacional de identidad número
                                        <strong>10.033.741-K</strong>, en adelante “EMPLEADOR”, y Sr(a) <strong>{{ $full_name }}</strong>, cédula nacional de identidad número
                                        <strong>{{ $rut }}</strong>, en adelante “TRABAJADOR”, quienes manifiestan haber convenido en la celebración del siguiente anexo de contrato de trabajo:<br><br>
                                        <strong>PRIMERO:</strong> Del Motivo. Las partes han pactado el otorgamiento de una asignación de remuneración denominado <strong>BONO META MENSUAL</strong>, el cual será pagado por Jis Parking como una forma de premiar la meta venta propuesta por la empresa.<br><br><br>
                                        <strong>SEGUNDO:</strong> Del Monto y condiciones. Jis Parking SPA y el Trabajador pactan que el BONO META MENSUAL será un incentivo económico al cual postulara de manera mensual para cumplir con el presupuesto de venta asignado para cada mes, donde existirán dos formas de pago según cumplimiento de ventas:<br><br><br>
                                        <center><img style="height: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/bonuses.png'))) }}"></center>
                                        Requisitos para postular a la bonificación:<br><br><br>
                                        •	Haber trabajado al menos 20 días durante el mes a cumplir la meta.<br><br><br>
                                        <strong>TERCERA:</strong> De las Cotizaciones. Para todos los efectos legales, el BONO META MENSUAL constituye remuneración imponible, por lo cual la empresa efectuará las deducciones legales correspondientes.<br><br><br>
                                        <strong>CUARTO:</strong> De la Suscripción. El presente anexo de contrato se firma en dos ejemplares del mismo tenor y fecha, quedando uno en poder del(la) trabajador(a) y otro en poder del empleador.<br>
                                        <br><br><br><br>
                                        <center><img style="width: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____________________</center>
                                        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
                                        <center>76.063.822-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}&nbsp;&nbsp;</center>
                                        <br><br><br><br><br><br><center><font style="font-size: 10px;">11 de 11</font></center>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        
                    </td>
                </tr>
            </tbody>
        </table>
     </body>
</html>