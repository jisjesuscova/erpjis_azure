$(document).ready(function () {
    $(document).ready(function() {
        $('.answered_row').hide();
        $("#total_answered_questions").text("0");
        if ($('#branch_office_id').val() == '' || $('#added_date').val() == '') {
            $('#questions_to_answer').hide();
        } else {
            $('#questions_to_answer').show();
        }

        $('#branch_office_id').change(function() {
            if ($('#branch_office_id').val() == '' || $('#added_date').val() == '') {
                $('#questions_to_answer').hide();
            } else {
                $('#questions_to_answer').show();
            }
        });

        $('#added_date').change(function() {
            if ($('#branch_office_id').val() == '' || $('#added_date').val() == '') {
                $('#questions_to_answer').hide();
            } else {
                $('#questions_to_answer').show();
            }
        });

        $('.guardar-btn').click(function(event) {
            event.preventDefault();
    
            // Obtener el ID de fila
            var rowId = $(this).data('row-id');
    
            // Mostrar el mensaje de "Cargando..."
            $(this).hide();
            $('span#loading-icon_' + rowId).show();

            // Crear un objeto FormData y agregar los datos del formulario
            var formData = new FormData();

            var radioButtons = $('input[name="answer_id_' + rowId + '"]');

            // Obtener el valor del radio button seleccionado
            var selectedValue = radioButtons.filter(':checked').val();

            var total_answered_questions = $("#total_answered_questions").text();
            var total_questions = $("#total_questions").text();

            formData.append('id', rowId);
            formData.append('check_group_question_id', $('#check_group_question_id').val());
            formData.append('check_group_question_detail_id', $('#check_group_question_detail_id_' + rowId).val());
            formData.append('branch_office_id', $('#branch_office_id').val());
            formData.append('added_date', $('#added_date').val());
            formData.append('answer_id', selectedValue);
            formData.append('description', $('#description_' + rowId).val());
            formData.append('file', $('input[name="file_' + rowId + '"]')[0].files[0]);
            
    
            // Enviar la solicitud AJAX
            $.ajax({
                url: "/check_answer/store",
                method: 'POST',
                headers: {
                    "X-CSRFToken": $('input[name="csrf_token_' + rowId + '"]').val()
                },
                data: formData,
                processData: false,
                contentType: false,
                success: function(response) {
                    // Actualizar la interfaz de usuario
                    $('span#loading-icon_' + rowId).hide();
                    $('.guardar-btn').show();
                    $('#no_answered_row_' + rowId).hide();
                    $('#answered_row_' + rowId).show();

                    total = parseInt(total_answered_questions) + 1;
                    $("#total_answered_questions").text(total)

                    if (parseInt(total) == parseInt(total_questions)) {
                        alert('La encuesta ha culminado con éxito. Muchas gracias.')
                        window.location.href = "http://localhost:5000/checks";
                    }
                },
                error: function() {
                    alert('Error al guardar los datos');
                }
            });
        });
    });

    $('.sigPad').signaturePad({drawOnly:true});

    $("#regime_afp").hide();
    $("#progressive_vacation_date").hide();

    $('body').on('mousemove', function(event) {
        var regime_id = $("#regime_id").val();
        var progressive_vacation_status_id = $("#progressive_vacation_status_id").val();

        if(regime_id == 1) {
            $("#regime_afp").show();
        } else {
            $("#regime_afp").hide();
        }

        if(progressive_vacation_status_id == 1) {
            $("#progressive_vacation_date").show();
        } else {
            $("#progressive_vacation_date").hide();
        }
    });

    var api = $('.sigPad').signaturePad();

    $('#save-button').click(function(){
        var dataUrl = api.getSignatureImage();

        $.ajax({
            type: "POST",
            url: '/signature/store',
            data: { signature: dataUrl },
            success: function(response) {
                window.location.href = 'http://127.0.0.1:5000/human_resources/personal_data/' + $('#rut').val();
            }
        });
    });

    $('#progressive_vacation_status_id').change(function() {
        var id = $(this).val()
        if(id == 1) {
            $("#progressive_vacation_date").show();
        } else {
            $("#progressive_vacation_date").hide();
        }
    });

    $('#regime_id').change(function() {
        var id = $(this).val()
        if(id == 1) {
            $("#regime_afp").show();
        } else {
            $("#regime_afp").hide();
        }
    });

    $('#slider').slick({
        arrows: true,
        prevArrow: '.slick-prev',
        nextArrow: '.slick-next'
    });

    $('#sign-button').prop("disabled", true);

    $(".modal").on("hidden.bs.modal", function() {
        location.reload();
    });

    $("#employee_status_id").change(function() {
        var employee_status_id = $(this).val();

        $(".employee_status_id").val(employee_status_id)
    });

    $("#causal_id").change(function() {
        var causal_id = $(this).val();

        $(".causal_id").val(causal_id)
    });

    $("#exit_company").change(function() {
        var exit_company = $(this).val();

        $(".exit_company").val(exit_company)
    });

    $("#number_holidays").change(function() {
        var number_holidays = $(this).val();

        $(".number_holidays").val(number_holidays)
    });

    $("#voluntary_indemnity").change(function() {
        var total

        var voluntary_indemnity = $(this).val();

        $(".voluntary_indemnity").val(voluntary_indemnity) 

        total = parseInt($("#voluntary_indemnity").val()) + parseInt($("#indemnity_years_service").val()) + parseInt($("#substitute_compensation").val()) + parseInt($("#fertility_proportional").val())

        $("#total").val(total)
    });

    $("#indemnity_years_service").change(function() {
        var total

        total = parseInt($("#voluntary_indemnity").val()) + parseInt($("#indemnity_years_service").val()) + parseInt($("#substitute_compensation").val()) + parseInt($("#fertility_proportional").val())

        $("#total").val(total)
    });

    $("#substitute_compensation").change(function() {
        var total

        total = parseInt($("#voluntary_indemnity").val()) + parseInt($("#indemnity_years_service").val()) + parseInt($("#substitute_compensation").val()) + parseInt($("#fertility_proportional").val())

        $("#total").val(total)
    });

    $("#fertility_proportional").change(function() {
        var total

        total = parseInt($("#voluntary_indemnity").val()) + parseInt($("#indemnity_years_service").val()) + parseInt($("#substitute_compensation").val()) + parseInt($("#fertility_proportional").val())

        $("#total").val(total)
    });

    $("#region_id").change(function() {
        var regionId = $(this).val();

        $.ajax({
          url: "/master_data/communes/region/" + regionId,
          type: "GET",
          success: function(communes) {
            $("#commune_id").empty();
            $.each(communes, function(key, commune) {
              $("#commune_id").append('<option value="' + commune.id + '">' + commune.commune + '</option>');
            });
          }
        });
    });
    
    $(".modal").on("hidden.bs.modal", function() {
        location.reload();
    });

    $('.rut').mask('99999999-9');

    $('#branch_office_id').change(function() {
        $.ajax({
            url: 'branch_offices/employees/' + $(this).val(),
            type: 'GET',
            success: function(data){
                data = JSON.parse(data)
                for (var i = 0; i < data.length; ++i) {
                    $('<option value="'+data[i].rut+'">'+data[i].nickname+'</option>').appendTo('#employee_id');
                }
            }
        });
    });

    $('#employee_id').change(function() {
        $.ajax({
            url: '/turns/types/' + $(this).val() + '/' + $('#group_id').val(),
            type: 'GET',
            success: function(data) {
                data = JSON.parse(data)
                console.log(data)
                $('#turns').empty();
                
                for (var i = 0; i < data.length; ++i) {
                    $('<div duration="'+ data[i].group_day_id +'" class="fc-event fc-h-event fc-daygrid-event fc-daygrid-block-event"><div class="fc-event-main"><center>Id: '+ data[i].id +' - Horario: '+ data[i].turn +'. Días: '+ data[i].group_day_id +'x' + data[i].free_day_group_id + '</center></div></div>').appendTo('#turns');
                }
            }
        });
    });

    $('#group_id').change(function() {
        $.ajax({
            url: '/turns/types/' + $('#employee_id').val() + '/' + $(this).val(),
            type: 'GET',
            success: function(data) {
                data = JSON.parse(data)
                $('#turns').empty();

                for (var i = 0; i < data.length; ++i) {
                    $('<div duration="'+ data[i].group_day_id +'" class="fc-event fc-h-event fc-daygrid-event fc-daygrid-block-event"><div class="fc-event-main"><center>Id: '+ data[i].id +' - Horario: '+ data[i].turn +'. Días: '+ data[i].group_day_id +'x' + data[i].free_day_group_id + '</center></div></div>').appendTo('#turns');
                }
            }
        });
    });
});