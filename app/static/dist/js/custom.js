$(document).ready(function () {
    $('.answered_row').hide();
    $('.replacement_honorary').hide();
    $('.displayed_replacement_honorary').show();
    $(".update-honorary-btn").prop("disabled", true);
    $('.full_time').show();
    $('.part_time').show();

    if ($("#exit_company").val() != null && $("#exit_company").val() != '') {
        $("#calculate_fertility_proportional").prop("disabled", false);
        $("#calculate_substitute_compensation").prop("disabled", false);
        $("#calculate_indemnity_years_service").prop("disabled", false);
    } else {
        $("#calculate_fertility_proportional").prop("disabled", true);
        $("#calculate_substitute_compensation").prop("disabled", true);
        $("#calculate_indemnity_years_service").prop("disabled", true);
    }
    
    $("#calculate_indemnity_years_service").click(function() {
        var formData = new FormData();
        
        formData.append('rut', $('#rut').val());
        formData.append('exit_company', $('#exit_company').val());

        $.ajax({
            url: "/human_resources/end_document/indemnity_years_service",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                $('#indemnity_years_service').val(response);

                return;
            }
        });
    });

    $("#calculate_substitute_compensation").click(function() {
        var formData = new FormData();
        
        formData.append('rut', $('#rut').val());

        $.ajax({
            url: "/human_resources/end_document/substitute_compensation",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                $('#substitute_compensation').val(response);

                return;
            }
        });
    });

    $("#calculate_fertility_proportional").click(function() {
        var formData = new FormData();
        
        formData.append('rut', $('#rut').val());
        formData.append('exit_company', $('#exit_company').val());
        formData.append('balance', $('#balance').val());
        formData.append('number_holidays', $('#number_holidays').val());
        
        $.ajax({
            url: "/human_resources/end_document/fertility_proportional",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                data = response.split("_");

                $('#fertility_proportional').val(data[0]);
                $('#fertility_proportional_days').val(data[1]);

                return;
            }
        });
    });

    $("#end_document_total").click(function() {
        $('#total').val(parseInt($('#substitute_compensation').val()) + parseInt($('#indemnity_years_service').val()) + parseInt($('#fertility_proportional').val()) + parseInt($('#voluntary_indemnity').val()));
    });

    $("#save_end_document").click(function() {
        var formData = new FormData();
        
        if ($('#employee_status_id').val() != '' 
            && $('#causal_id').val() != "" 
            && $('#exit_company').val() != ""
            && $('#balance').val() != ""
        ) {
            formData.append('rut', $('#rut').val());
            formData.append('employee_status_id', $('#employee_status_id').val());
            formData.append('causal_id', $('#causal_id').val());
            formData.append('exit_company', $('#exit_company').val());
            formData.append('balance', $('#balance').val());
            formData.append('voluntary_indemnity', $('#voluntary_indemnity').val());
            formData.append('indemnity_years_service', $('#indemnity_years_service').val());
            formData.append('substitute_compensation', $('#substitute_compensation').val());
            formData.append('fertility_proportional', $('#fertility_proportional').val());
            formData.append('fertility_proportional_days', $('#fertility_proportional_days').val());
            formData.append('number_holidays', $('#number_holidays').val());
            formData.append('total', $('#total').val());
            formData.append('status_id', 3);
            formData.append('document_type_id', 22);
            
            $.ajax({
                url: "/human_resources/end_document/store",
                method: 'POST',
                headers: {
                    "X-CSRFToken": $('input[name="csrf_token"]').val()
                },
                data: formData,
                processData: false,
                contentType: false,
                success: function(response) {
                    if (response == 1) {
                        window.location.replace("https://jiserp.com/human_resources/personal_data/" + $("#rut").val());
                    } else {
                        alert("No se pudo completar la transacción.");
                    }

                    return;
                }
            });
        }
    });

    $('[data-toggle="tooltip"]').tooltip()

    $("#description").on("keyup", function() {
        $("#markdown_view").html(marked($(this).val()));
    });

    $("#description").focusout(function(){
        $("#markdown_view").html(marked($(this).val()));
    });

    $("#description").focusin(function(){
        $("#markdown_view").html(marked($(this).val()));
    });

    $("#reason_id").change(function(){
        if ($("#reason_id").val() == 2 || $("#reason_id").val() == 3 || $("#reason_id").val() == 4) {
            $('.replacement_honorary').show();
            $('.displayed_replacement_honorary').show();
        } else {
            $('.replacement_honorary').hide();
            $('.displayed_replacement_honorary').hide();
        }
    });

    $("#employee_type_id").change(function(){
        $('#job_position_id').prop('selectedIndex', 0);
        if ($(this).val() == 1) {
            $('.full_time').show();
            $('.part_time').hide();
        } else {
            $('.full_time').hide();
            $('.part_time').show();
        }
    });

    $("#exit_company").change(function(){
        if($(this).val() != '' && $(this).val() != null) {
            $("#calculate_fertility_proportional").prop("disabled", false);
            $("#calculate_substitute_compensation").prop("disabled", false);
            $("#calculate_indemnity_years_service").prop("disabled", false);
        }
    });

    $("#job_position_id").change(function(){
        if($(this).val() != 10 && $(this).val() != 9 &&  $(this).val() != 8 &&  $(this).val() != 7 && $(this).val() != 6) {
            $("#create-contract").hide();
        } else {
            $("#create-contract").show();
        }
    });

    $("#are_you_sure").change(function(){
        if ($("#are_you_sure").val() == 1) {
            $(".update-honorary-btn").prop("disabled", false);
        } else {
            $(".update-honorary-btn").prop("disabled", true);
        }
    });

    function validateRut(rut) {
        // Remove dots and dashes from the RUT (if any)
        rut = rut.replace(/[.-]/g, "");
    
        // Extract the check digit from the RUT
        var dv = rut.slice(-1);
    
        // Extract the digits before the check digit from the RUT
        var rutWithoutDv = rut.slice(0, -1);
    
        // Calculate the expected check digit for the digits before the check digit
        var sum = 0;
        var multiplier = 2;
        for (var i = rutWithoutDv.length - 1; i >= 0; i--) {
            sum += rutWithoutDv.charAt(i) * multiplier;
            if (multiplier < 7) {
                multiplier++;
            } else {
                multiplier = 2;
            }
        }
        var expectedDv = 11 - (sum % 11);
        if (expectedDv == 11) {
            expectedDv = 0;
        } else if (expectedDv == 10) {
            expectedDv = "K";
        }
    
        // Convert k to K
        dv = dv.toUpperCase();
    
        // Compare the expected check digit with the actual check digit
        if (dv == expectedDv) {
            return true;
        } else {
            return false;
        }
    }

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

    $("#rut").focusout(function() {
        var hasRutField = false;
        if (validateRut($("#rut").val())){
            hasRutField = false;
        } else {
            hasRutField = true;
        }

        if (hasRutField) {
            $('.alert-rut-form').show();
            return;
        } else {
            $('.alert-rut-form').hide();
        }

        var formData = new FormData();
        
        formData.append('rut', $('#rut').val());

        $.ajax({
            url: "/human_resources/employee/check_rut",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == '1') {
                    $('.alert-danger-cellphone-form').hide();
                    $('.alert-danger-form').hide();
                    $('.alert-danger-rut-exist-form').show();
                    $('.alert-danger-cellphone-exist-form').hide();
                    $('span#loading-icon').hide();
                    $('.create-user-btn').show();
                    $(".create-user-btn").prop("disabled", true);
                    $('.alert-rut-form').hide();
                } else {
                    $(".create-user-btn").prop("disabled", false);
                    $('span#loading-icon').hide();
                    $('.create-user-btn').show();
                    $('.alert-danger-rut-exist-form').hide();
                }

                return;
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-cellphone-form').hide();
                $('.alert-danger-form').hide();
                $('.alert-danger-rut-exist-form').hide();
                $('.alert-danger-cellphone-exist-form').hide();
                $('span#loading-icon').hide();
                $('.create-user-btn').show();
                $('.alert-rut-form').hide();
            }
        });
    });

    $("#rut").mouseout(function() {
        var hasRutField = false;
        if (validateRut($("#rut").val())){
            hasRutField = false;
        } else {
            hasRutField = true;
        }

        if (hasRutField) {
            $('.alert-rut-form').show();
            return;
        } else {
            $('.alert-rut-form').hide();
        }

        var formData = new FormData();
        
        formData.append('rut', $('#rut').val());

        $.ajax({
            url: "/human_resources/employee/check_rut",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == '1') {
                    $('.alert-danger-cellphone-form').hide();
                    $('.alert-danger-form').hide();
                    $('.alert-danger-rut-exist-form').show();
                    $('.alert-danger-cellphone-exist-form').hide();
                    $('span#loading-icon').hide();
                    $('.create-user-btn').show();
                    $(".create-user-btn").prop("disabled", true);
                    $('.alert-rut-form').hide();
                } else {
                    $(".create-user-btn").prop("disabled", false);
                    $('span#loading-icon').hide();
                    $('.create-user-btn').show();
                    $('.alert-danger-rut-exist-form').hide();
                }

                return;
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-cellphone-form').hide();
                $('.alert-danger-form').hide();
                $('.alert-danger-rut-exist-form').hide();
                $('.alert-danger-cellphone-exist-form').hide();
                $('span#loading-icon').hide();
                $('.create-user-btn').show();
                $('.alert-rut-form').hide();
            }
        });
    });

    $("#cellphone").focusout(function() {
        var formData = new FormData();
            
        formData.append('cellphone', $('#cellphone').val());

        $.ajax({
            url: "/human_resources/employee/check_cellphone",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                var isDisabled = $(".create-user-btn").prop("disabled");

                if (!isDisabled) {
                    if (response == 1) {
                        $('.alert-danger-cellphone-form').hide();
                        $('.alert-danger-form').hide();
                        $('.alert-danger-rut-exist-form').hide();
                        $('.alert-danger-cellphone-exist-form').show();
                        $('span#loading-icon').hide();
                        $('.create-user-btn').show();
                        $(".create-user-btn").prop("disabled", true);
    
                        return;
                    } else {
                        $(".create-user-btn").prop("disabled", false);
                        $('.alert-danger-cellphone-exist-form').hide();
                        $('span#loading-icon').hide();
                        $('.create-user-btn').show();
                        return;
                    }
                }
                
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-cellphone-form').hide();
                $('.alert-danger-form').hide();
                $('.alert-danger-rut-exist-form').hide();
                $('.alert-danger-cellphone-exist-form').hide();
                $('span#loading-icon').hide();
                $('.create-user-btn').show();
            }
         });
    });

    $("#cellphone").mouseout(function() {
        var formData = new FormData();
            
        formData.append('cellphone', $('#cellphone').val());

        $.ajax({
            url: "/human_resources/employee/check_cellphone",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                var isDisabled = $(".create-user-btn").prop("disabled");

                if (!isDisabled) {
                    if (response == 1) {
                        $('.alert-danger-cellphone-form').hide();
                        $('.alert-danger-form').hide();
                        $('.alert-danger-rut-exist-form').hide();
                        $('.alert-danger-cellphone-exist-form').show();
                        $('span#loading-icon').hide();
                        $('.create-user-btn').show();
                        $(".create-user-btn").prop("disabled", true);
                        $('.update-user-btn').show();
                        $(".update-user-btn").prop("disabled", true);
    
                        return;
                    } else {
                        $(".create-user-btn").prop("disabled", false);
                        $(".update-user-btn").prop("disabled", false);
                        $('.alert-danger-cellphone-exist-form').hide();
                        $('span#loading-icon').hide();
                        $('.create-user-btn').show();
                        $('.update-user-btn').show();
                        return;
                    }
                }
                
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-cellphone-form').hide();
                $('.alert-danger-form').hide();
                $('.alert-danger-rut-exist-form').hide();
                $('.alert-danger-cellphone-exist-form').hide();
                $('span#loading-icon').hide();
                $('.create-user-btn').show();
                $('.update-user-btn').show();
            }
         });
    });

    $('.accept-bank-account-btn').click(function(event) {
        var formData = new FormData();

        $('span#loading-icon').show();
        $('.accept-bank-account-btn').hide();

        formData.append('requested_employee_bank_account_id', $("#requested_employee_bank_account_id").val());

        $.ajax({
            url: "/human_resources/employee_bank_account/accept/" + $("#requested_employee_bank_account_id").val(),
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/personal_data/" + $("#numeric_rut").val());
                } else {
                    $('span#loading-icon').hide();
                    $('.accept-bank-account-btn').show();
                }
            },
            error: function() {
                $('span#loading-icon').hide();
                $('.accept-bank-account-btn').show();
            }
        });
    });

    $('.reject-bank-account-btn').click(function(event) {
        var formData = new FormData();

        $('span#loading-icon').show();
        $('.reject-bank-account-btn').hide();

        formData.append('requested_employee_bank_account_id', $("#requested_employee_bank_account_id").val());

        $.ajax({
            url: "/human_resources/employee_bank_account/reject/" + $("#requested_employee_bank_account_id").val(),
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/personal_data/" + $("#numeric_rut").val());
                } else {
                    $('span#loading-icon').hide();
                    $('.reject-bank-account-btn').show();
                }
            },
            error: function() {
                $('span#loading-icon').hide();
                $('.reject-bank-account-btn').show();
            }
        });
    });

    $('.create-bank-account-btn').click(function(event) {
        var formData = new FormData();

        $('span#loading-icon').show();
        $('.create-bank-account-btn').hide();

        formData.append('rut', $("#numeric_rut").val());
        formData.append('account_type_id', $("#account_type_id").val());
        formData.append('bank_id', $("#bank_id").val());
        formData.append('account_number', $("#account_number").val());

        $.ajax({
            url: "/human_resources/employee_bank_account/store",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/personal_data/" + $("#numeric_rut").val());
                } else {
                    $('span#loading-icon').hide();
                    $('.create-bank-account-btn').show();
                }
            },
            error: function() {
                $('span#loading-icon').hide();
                $('.create-bank-account-btn').show();
            }
        });
    });

    $('.create-mesh-btn').click(function(event) {
        var formData = new FormData();

        $('span#loading-icon').show();
        $('.create-mesh-btn').hide();

        formData.append('rut', $("#employee_id").val());

        $.ajax({
            url: "/mesh_data/store",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/mesh_data");
                } else {
                    $('span#loading-icon').hide();
                    $('.create-mesh-btn').show();
                }
            },
            error: function() {
                $('span#loading-icon').hide();
                $('.create-mesh-btn').show();
            }
        });
    });

    $('.update-honorary-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['reason_id', 'branch_office_id', 'start_date', 'end_date', 'rut', 'full_name', 'email', 'region_id', 'commune_id', 'address', 'foreigner_id', 'bank_id', 'account_number', 'schedule_id', 'observation', 'amount'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        var hasRutField = false;
        if (validateRut($("#rut").val())){
            hasRutField = false;
        } else {
            hasRutField = true;
        }

        if (hasRutField) {
            $('.alert-rut-form').show();
            return;
        } else {
            $('.alert-rut-form').hide();
        }

        $('span#loading-icon').show();
        $('.update-honorary-btn').hide();
        
        var formData = new FormData();
        formData.append('id', $('#id').val());
        formData.append('reason_id', $('#reason_id').val());
        formData.append('branch_office_id', $('#branch_office_id').val());
        formData.append('employee_to_replace', $('#employee_id').val());
        formData.append('start_date', $('#start_date').val());
        formData.append('end_date', $('#end_date').val()); 
        formData.append('rut', $('#rut').val());
        formData.append('full_name', $('#full_name').val());
        formData.append('email', $('#email').val());
        formData.append('region_id', $('#region_id').val());
        formData.append('commune_id', $('#commune_id').val());
        formData.append('address', $('#address').val());
        formData.append('foreigner_id', $('#foreigner_id').val());
        formData.append('bank_id', $('#bank_id').val());
        formData.append('account_number', $('#account_number').val());
        formData.append('schedule_id', $('#schedule_id').val());
        formData.append('observation', $('#observation').val());
        formData.append('amount', $('#amount').val());

        $.ajax({
            url: "/human_resources/honorary/update/" + $('#id').val(),
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/honoraries");
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-cellphone-form').hide();
                    $('.alert-danger-form').hide();
                    $('.alert-danger-rut-exist-form').hide();
                    $('.alert-danger-cellphone-exist-form').hide();
                    $('span#loading-icon').hide();
                    $('.update-honorary-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-cellphone-form').hide();
                $('.alert-danger-form').hide();
                $('.alert-danger-rut-exist-form').hide();
                $('.alert-danger-cellphone-exist-form').hide();
                $('span#loading-icon').hide();
                $('.update-honorary-btn').show();
            }
        });
    });

    $('.create-honorary-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['reason_id', 'branch_office_id', 'start_date', 'end_date', 'rut', 'full_name', 'email', 'region_id', 'commune_id', 'address', 'foreigner_id', 'bank_id', 'account_number', 'schedule_id', 'observation'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        var hasRutField = false;
        if (validateRut($("#rut").val())){
            hasRutField = false;
        } else {
            hasRutField = true;
        }

        if (hasRutField) {
            $('.alert-rut-form').show();
            return;
        } else {
            $('.alert-rut-form').hide();
        }

        $('span#loading-icon').show();
        $('.create-honorary-btn').hide();
        
        var formData = new FormData();
        
        formData.append('reason_id', $('#reason_id').val());
        formData.append('branch_office_id', $('#branch_office_id').val());
        formData.append('employee_to_replace', $('#employee_id').val());
        formData.append('start_date', $('#start_date').val());
        formData.append('end_date', $('#end_date').val()); 
        formData.append('rut', $('#rut').val());
        formData.append('full_name', $('#full_name').val());
        formData.append('email', $('#email').val());
        formData.append('region_id', $('#region_id').val());
        formData.append('commune_id', $('#commune_id').val());
        formData.append('address', $('#address').val());
        formData.append('foreigner_id', $('#foreigner_id').val());
        formData.append('bank_id', $('#bank_id').val());
        formData.append('account_number', $('#account_number').val());
        formData.append('schedule_id', $('#schedule_id').val());
        formData.append('observation', $('#observation').val());

        $.ajax({
            url: "/human_resources/honorary/store",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/honoraries");
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-cellphone-form').hide();
                    $('.alert-danger-form').hide();
                    $('.alert-danger-rut-exist-form').hide();
                    $('.alert-danger-cellphone-exist-form').hide();
                    $('span#loading-icon').hide();
                    $('.create-honorary-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-cellphone-form').hide();
                $('.alert-danger-form').hide();
                $('.alert-danger-rut-exist-form').hide();
                $('.alert-danger-cellphone-exist-form').hide();
                $('span#loading-icon').hide();
                $('.create-honorary-btn').show();
            }
        });
    });

    $('.update-user-btn').click(function(event) {
        event.preventDefault();

        if ($('#rol_id').val() != 1) {
            // Verificar si hay campos vacíos o indefinidos
            var requiredFields = ['names', 'father_lastname', 'mother_lastname', 'gender_id', 'nationality_id', 'personal_email', 'cellphone', 'born_date'];
            var hasEmptyField = false;
            for (var i = 0; i < requiredFields.length; i++) {
                var field = $('#' + requiredFields[i]);
                if (field.val() === '' || typeof field.val() === 'undefined') {
                    hasEmptyField = true;
                    break;
                }
            }

            if (hasEmptyField) {
                $('.alert-danger-form').show();
                return;
            }

            var cellphone = $('#cellphone').val();
            if (cellphone.length < 9) {
                $('.alert-danger-cellphone-form').show();
                $('.alert-danger-form').hide();
                return;
            }
        }

        $('span#loading-icon').show();
        $('.update-user-btn').hide();
        
        var formData = new FormData();
        formData.append('rut', $('#numeric_rut').val());
        formData.append('names', $('#names').val());
        formData.append('father_lastname', $('#father_lastname').val());
        formData.append('mother_lastname', $('#mother_lastname').val());
        formData.append('gender_id', $('#gender_id').val()); 
        formData.append('nationality_id', $('#nationality_id').val());
        formData.append('personal_email', $('#personal_email').val());
        formData.append('cellphone', $('#cellphone').val());
        formData.append('born_date', $('#born_date').val());
        formData.append('success_update_id', 1);

        $.ajax({
            url: "/human_resources/personal_data/"+$('#numeric_rut').val(),
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/personal_data/"+$('#numeric_rut').val());
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-cellphone-form').hide();
                    $('.alert-danger-form').hide();
                    $('.alert-danger-rut-exist-form').hide();
                    $('.alert-danger-cellphone-exist-form').hide();
                    $('span#loading-icon').hide();
                    $('.update-user-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-cellphone-form').hide();
                $('.alert-danger-form').hide();
                $('.alert-danger-rut-exist-form').hide();
                $('.alert-danger-cellphone-exist-form').hide();
                $('span#loading-icon').hide();
                $('.update-user-btn').show();
            }
        });
    });

    $('.create-user-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['rut', 'names', 'father_lastname', 'mother_lastname', 'gender_id', 'nationality_id', 'personal_email', 'cellphone', 'born_date', 'privilege'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        var cellphone = $('#cellphone').val();
        if (cellphone.length < 9) {
            $('.alert-danger-cellphone-form').show();
            $('.alert-danger-form').hide();
            return;
        }

        $('span#loading-icon').show();
        $('.create-user-btn').hide();
        
        var formData = new FormData();
        var rut =  $('#rut').val()

        rut = rut.split('-')
        rut = rut[0]
        
        formData.append('rut', $('#rut').val());
        formData.append('names', $('#names').val());
        formData.append('father_lastname', $('#father_lastname').val());
        formData.append('mother_lastname', $('#mother_lastname').val());
        formData.append('gender_id', $('#gender_id').val()); 
        formData.append('nationality_id', $('#nationality_id').val());
        formData.append('personal_email', $('#personal_email').val());
        formData.append('cellphone', $('#cellphone').val());
        formData.append('born_date', $('#born_date').val());
        formData.append('privilege', $('#privilege').val());
        formData.append('uid', $('#uid').val());
        formData.append('entrance_company', $('#entrance_company').val());
        formData.append('success_store_id', 1);

        $.ajax({
            url: "/human_resources/employee/store",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/personal_data/"+rut);
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-cellphone-form').hide();
                    $('.alert-danger-form').hide();
                    $('.alert-danger-rut-exist-form').hide();
                    $('.alert-danger-cellphone-exist-form').hide();
                    $('span#loading-icon').hide();
                    $('.create-user-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-cellphone-form').hide();
                $('.alert-danger-form').hide();
                $('.alert-danger-rut-exist-form').hide();
                $('.alert-danger-cellphone-exist-form').hide();
                $('span#loading-icon').hide();
                $('.create-user-btn').show();
            }
        });
    });

    $('.create-vacation-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['since', 'until', 'no_valid_days'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        $('span#loading-icon').show();
        $('.create-vacation-btn').hide();
        
        var formData = new FormData();
        var rut =  $('#rut').val()

        rut = rut.split('-')
        rut = rut[0]
        
        formData.append('rut', $('#rut').val());
        formData.append('since', $('#since').val());
        formData.append('until', $('#until').val());
        formData.append('no_valid_days', $('#no_valid_days').val());
        formData.append('document_type_id', $('#document_type_id').val()); 
        formData.append('status_id', $('#status_id').val());

        $.ajax({
            url: "/human_resources/vacation/store",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/vacations/"+rut);
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-form').hide();
                    $('span#loading-icon').hide();
                    $('.create-vacation-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-form').hide();
                $('span#loading-icon').hide();
                $('.create-vacation-btn').show();
            }
        });
    });

    $('.create-license-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['folio', 'medical_license_type_id', 'patology_type_id', 'since', 'until', 'file'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        $('span#loading-icon').show();
        $('.create-license-btn').hide();
        
        var formData = new FormData();
        var rut =  $('#rut').val()

        rut = rut.split('-')
        rut = rut[0]
        
        formData.append('rut', $('#rut').val());
        formData.append('status_id', $('#status_id').val());
        formData.append('document_type_id', $('#document_type_id').val());
        formData.append('folio', $('#folio').val());
        formData.append('medical_license_type_id', $('#medical_license_type_id').val()); 
        formData.append('patology_type_id', $('#patology_type_id').val());
        formData.append('since', $('#since').val());
        formData.append('until', $('#until').val());
        formData.append('file', $('input[name="file"]')[0].files[0]);

        $.ajax({
            url: "/human_resources/medical_license/store/" + $('#rut').val(),
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/medical_licenses/"+rut);
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-form').hide();
                    $('span#loading-icon').hide();
                    $('.create-license-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-form').hide();
                $('span#loading-icon').hide();
                $('.create-license-btn').show();
            }
        });
    });

    $('.upload-vacation-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['file'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        $('span#loading-icon').show();
        $('.upload-vacation-btn').hide();
        
        var formData = new FormData();
        var rut =  $('#rut').val()

        rut = rut.split('-')
        rut = rut[0]
        
        formData.append('file', $('input[name="file"]')[0].files[0]);

        $.ajax({
            url: "/human_resources/vacation/upload/" + rut,
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/vacation/"+rut);
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-form').hide();
                    $('span#loading-icon').hide();
                    $('.upload-vacation-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-form').hide();
                $('span#loading-icon').hide();
                $('.upload-vacation-btn').show();
            }
        });
    });

    $('.upload-license-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['file'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        $('span#loading-icon').show();
        $('.upload-license-btn').hide();
        
        var formData = new FormData();
        var rut =  $('#rut').val()

        rut = rut.split('-')
        rut = rut[0]
        
        formData.append('id', $('#id').val());
        formData.append('rut', $('#rut').val());
        formData.append('file', $('input[name="file"]')[0].files[0]);

        $.ajax({
            url: "/human_resources/medical_license/upload/" + $('#id').val() + "/" + $('#rut').val(),
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/medical_licenses/"+rut);
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-form').hide();
                    $('span#loading-icon').hide();
                    $('.upload-license-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-form').hide();
                $('span#loading-icon').hide();
                $('.upload-license-btn').show();
            }
        });
    });

    $('.update-user-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['names', 'father_lastname', 'mother_lastname', 'gender_id', 'nationality_id', 'personal_email', 'cellphone', 'born_date'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        var cellphone = $('#cellphone').val();
        if (cellphone.length < 9) {
            $('.alert-danger-cellphone-form').show();
            $('.alert-danger-form').hide();
            return;
        }

        $('span#loading-icon').show();
        $('.update-user-btn').hide();
        
        var formData = new FormData();
        var rut =  $('#rut').val()

        rut = rut.split('-')
        rut = rut[0]
        
        formData.append('names', $('#names').val());
        formData.append('father_lastname', $('#father_lastname').val());
        formData.append('mother_lastname', $('#mother_lastname').val());
        formData.append('gender_id', $('#gender_id').val()); 
        formData.append('nationality_id', $('#nationality_id').val());
        formData.append('personal_email', $('#personal_email').val());
        formData.append('cellphone', $('#cellphone').val());
        formData.append('born_date', $('#born_date').val());
        formData.append('file', $('input[name="file"]')[0].files[0]);
        formData.append('success_update_id', 1);

        $.ajax({
            url: "/human_resources/personal_data/" + rut,
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/personal_data/"+rut);
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-cellphone-form').hide();
                    $('.alert-danger-form').hide();
                    $('.alert-danger-rut-exist-form').hide();
                    $('.alert-danger-cellphone-exist-form').hide();
                    $('span#loading-icon').hide();
                    $('.update-user-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-cellphone-form').hide();
                $('.alert-danger-form').hide();
                $('.alert-danger-rut-exist-form').hide();
                $('.alert-danger-cellphone-exist-form').hide();
                $('span#loading-icon').hide();
                $('.update-user-btn').show();
            }
        });
    });

    $('.update-contract-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['contract_type_id', 'branch_office_id', 'region_id', 'commune_id', 'address', 'civil_state_id', 'entrance_health', 'job_position_id', 'entrance_company', 'salary', 'collation', 'locomotion', 'employee_type_id', 'regime_id', 'health_id'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        $('span#loading-icon').show();
        $('.update-contract-btn').hide();
        
        var formData = new FormData();
        var rut =  $('#rut').val()
        
        formData.append('rut', $('#rut').val());
        formData.append('contract_type_id', $('#contract_type_id').val());
        formData.append('branch_office_id', $('#branch_office_id').val());
        formData.append('region_id', $('#region_id').val());
        formData.append('commune_id', $('#commune_id').val()); 
        formData.append('address', $('#address').val());
        formData.append('civil_state_id', $('#civil_state_id').val());
        formData.append('entrance_health', $('#entrance_health').val());
        formData.append('job_position_id', $('#job_position_id').val());
        formData.append('entrance_company', $('#entrance_company').val());
        formData.append('salary', $('#salary').val());
        formData.append('collation', $('#collation').val());
        formData.append('locomotion', $('#locomotion').val());
        formData.append('employee_type_id', $('#employee_type_id').val());
        formData.append('regime_id', $('#regime_id').val());
        formData.append('health_id', $('#health_id').val());
        formData.append('pention_id', $('#pention_id').val());
        formData.append('entrance_pention', $('#entrance_pention').val());
        formData.append('health_payment_id', $('#health_payment_id').val());
        formData.append('extra_health_amount', $('#extra_health_amount').val());
        formData.append('apv_payment_type_id', $('#apv_payment_type_id').val());
        formData.append('apv_amount', $('#apv_amount').val());

        $.ajax({
            url: "/human_resources/contract_data/" + rut,
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/contract_data/"+rut);
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-form').hide();
                    $('span#loading-icon').hide();
                    $('.update-contract-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-form').hide();
                $('span#loading-icon').hide();
                $('.update-contract-btn').show();
            }
        });
    });

    $('.create-uniform-data-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['uniform_type_id', 'delivered_date'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        $('span#loading-icon').show();
        $('.create-uniform-data-btn').hide();
        
        var formData = new FormData();
        var rut =  $('#rut').val()
        
        formData.append('rut', $('#rut').val());
        formData.append('uniform_type_id', $('#uniform_type_id').val());
        formData.append('delivered_date', $('#delivered_date').val());

        $.ajax({
            url: "/human_resources/uniform/store",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/uniform/"+rut);
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-form').hide();
                    $('span#loading-icon').hide();
                    $('.create-uniform-data-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-form').hide();
                $('span#loading-icon').hide();
                $('.create-uniform-data-btn').show();
            }
        });
    });

    $('.create-kardex-data-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['document_type_id', 'file'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        $('span#loading-icon').show();
        $('.create-kardex-data-btn').hide();
        
        var formData = new FormData();
        var rut =  $('#rut').val()
        
        formData.append('rut', $('#rut').val());
        formData.append('document_type_id', $('#document_type_id').val());
        formData.append('file', $('input[name="file"]')[0].files[0]);

        $.ajax({
            url: "/human_resources/kardex_datum/store",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/kardex_data/"+rut);
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-form').hide();
                    $('span#loading-icon').hide();
                    $('.create-kardex-data-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-form').hide();
                $('span#loading-icon').hide();
                $('.create-kardex-data-btn').show();
            }
        });
    });

    $('.upload-vacation-data-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['file'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        $('span#loading-icon').show();
        $('.upload-vacation-data-btn').hide();
        
        var formData = new FormData();
        var rut =  $('#rut').val()
        
        formData.append('rut', $('#rut').val());
        formData.append('id', $('#id').val());
        formData.append('file', $('input[name="file"]')[0].files[0]);

        $.ajax({
            url: "/human_resources/documental_management_data/upload_vacation",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/vacations/"+rut);
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-form').hide();
                    $('span#loading-icon').hide();
                    $('.upload-vacation-data-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-form').hide();
                $('span#loading-icon').hide();
                $('.upload-vacation-data-btn').show();
            }
        });
    });

    $('.update-family-data-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['family_rut', 'names', 'father_lastname', 'mother_lastname', 'born_date', 'gender_id', 'family_type_id'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        var hasRutField = false;
        if (validateRut($("#rut").val())){
            hasRutField = false;
        } else {
            hasRutField = true;
        }

        if (hasRutField) {
            $('.alert-rut-form').show();
            return;
        } else {
            $('.alert-rut-form').hide();
        }

        $('span#loading-icon').show();
        $('.update-family-data-btn').hide();
        
        var formData = new FormData();
        var rut =  $('#rut').val()
        
        formData.append('rut', $('#user_rut').val());
        formData.append('id', $('#id').val());
        formData.append('family_rut', $('#rut').val());
        formData.append('names', $('#names').val());
        formData.append('father_lastname', $('#father_lastname').val());
        formData.append('mother_lastname', $('#mother_lastname').val()); 
        formData.append('born_date', $('#born_date').val());
        formData.append('gender_id', $('#gender_id').val());
        formData.append('family_type_id', $('#family_type_id').val());
        formData.append('file', $('input[name="file"]')[0].files[0]);

        $.ajax({
            url: "/human_resources/family_core_data/update/" + $('#rut').val() + "/" + $('#id').val(),
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/family_core_data/"+rut);
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-form').hide();
                    $('span#loading-icon').hide();
                    $('.update-family-data-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-form').hide();
                $('span#loading-icon').hide();
                $('.update-family-data-btn').show();
            }
        });
    });

    $('.create-family-data-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['rut', 'names', 'father_lastname', 'mother_lastname', 'born_date', 'gender_id', 'family_type_id', 'file'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        var hasRutField = false;
        if (validateRut($("#rut").val())){
            hasRutField = false;
        } else {
            hasRutField = true;
        }

        if (hasRutField) {
            $('.alert-rut-form').show();
            return;
        } else {
            $('.alert-rut-form').hide();
        }

        $('span#loading-icon').show();
        $('.create-family-data-btn').hide();
        
        var formData = new FormData();
        var rut =  $('#user_rut').val()
        
        formData.append('rut', $('#user_rut').val());
        formData.append('family_rut', $('#rut').val());
        formData.append('names', $('#names').val());
        formData.append('father_lastname', $('#father_lastname').val());
        formData.append('mother_lastname', $('#mother_lastname').val()); 
        formData.append('born_date', $('#born_date').val());
        formData.append('gender_id', $('#gender_id').val());
        formData.append('family_type_id', $('#family_type_id').val());
        formData.append('file', $('input[name="file"]')[0].files[0]);

        $.ajax({
            url: "/human_resources/family_core_datum/store",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/family_core_data/"+rut);
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-form').hide();
                    $('span#loading-icon').hide();
                    $('.create-family-data-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-form').hide();
                $('span#loading-icon').hide();
                $('.create-family-data-btn').show();
            }
        });
    });

    $('#my-form').submit(function(event) {
        event.preventDefault();
        
        var formData = new FormData();
        formData.append('month', $('#month').val());
        formData.append('year', $('#year').val());
        
        // Agregar los archivos al objeto FormData
        var files = $('input[name="file"]')[0].files;
        for (var i = 0; i < files.length; i++) {
            formData.append('files[]', files[i]);
        }
        
        // Enviar la solicitud AJAX
        $.ajax({
            url: '/management_payroll/settlement_data/store',
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                console.log(response);
            }
        });
    });

    $('.upload-settlement-data-btn').click(function(event) {
        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['month', 'year', 'file'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.upload-settlement-data-btn').show();
            $('span#loading-icon').hide();
        } else {
            $('.upload-settlement-data-btn').hide();
            $('span#loading-icon').show();
        }

        
    });

    $('.update-extra-data-btn').click(function(event) {
        event.preventDefault();
        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['extreme_zone_id', 'employee_type_id', 'young_job_status_id', 'be_paid_id', 'disability_id', 'pensioner_id'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        $('span#loading-icon').show();
        $('.update-extra-data-btn').hide();
        
        var formData = new FormData();
        var rut =  $('#rut').val()
        
        formData.append('rut', $('#rut').val());
        formData.append('extreme_zone_id', $('#extreme_zone_id').val());
        formData.append('employee_type_id', $('#employee_type_id').val());
        formData.append('young_job_status_id', $('#young_job_status_id').val()); 
        formData.append('be_paid_id', $('#be_paid_id').val());
        formData.append('disability_id', $('#disability_id').val());
        formData.append('pensioner_id', $('#pensioner_id').val());
        formData.append('progressive_vacation_status_id', $('#progressive_vacation_status_id').val());
        formData.append('progressive_vacation_date', $('#progressive_vacation_date_value').val());
        formData.append('suplemental_health_insurance_id', $('#suplemental_health_insurance_id').val());
        formData.append('recognized_years', $('#recognized_years').val());

        $.ajax({
            url: "/human_resources/employee_extra_data/" + rut,
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                console.log(response)
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/employee_extra_data/"+rut);
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-form').hide();
                    $('span#loading-icon').hide();
                    $('.update-extra-data-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-form').hide();
                $('span#loading-icon').hide();
                $('.update-extra-data-btn').show();
            }
        });
    });

    $('.create-end-document-btn').click(function(event) {
        event.preventDefault();

        // Verificar si hay campos vacíos o indefinidos
        var requiredFields = ['employee_status_id', 'causal_id', 'exit_company', 'number_holidays', 'voluntary_indemnity'];
        var hasEmptyField = false;
        for (var i = 0; i < requiredFields.length; i++) {
            var field = $('#' + requiredFields[i]);
            if (field.val() === '' || typeof field.val() === 'undefined') {
                hasEmptyField = true;
                break;
            }
        }

        if (hasEmptyField) {
            $('.alert-danger-form').show();
            return;
        }

        $('span#loading-icon').show();
        $('.create-end-document-btn').hide();
        
        var formData = new FormData();
        var rut =  $('#rut').val()
        
        formData.append('employee_status_id', $('#employee_status_id').val());
        formData.append('causal_id', $('#causal_id').val());
        formData.append('exit_company', $('#exit_company').val());
        formData.append('number_holidays', $('#number_holidays').val());
        formData.append('voluntary_indemnity', $('#voluntary_indemnity').val()); 
        formData.append('number_holidays', $('#number_holidays').val());
        formData.append('voluntary_indemnity', $('#voluntary_indemnity').val());
        formData.append('indemnity_years_service', $('#indemnity_years_service').val());
        formData.append('fertility_proportional', $('#fertility_proportional').val());
        formData.append('document_type_id', $('#document_type_id').val());
        formData.append('status_id', $('#status_id').val());
        formData.append('rut', $('#rut').val());
        formData.append('total', $('#total').val());
        formData.append('substitute_compensation', $('#substitute_compensation').val());

        $.ajax({
            url: "/human_resources/end_document/store",
            method: 'POST',
            headers: {
                "X-CSRFToken": $('input[name="csrf_token"]').val()
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response == 1) {
                    window.location.replace("https://jiserp.com/human_resources/contract_data/"+rut);
                } else {
                    $('.alert-danger-404-form').show();
                    $('.alert-danger-form').hide();
                    $('span#loading-icon').hide();
                    $('.create-end-document-btn').show();
                }
            },
            error: function() {
                $('.alert-danger-404-form').show();
                $('.alert-danger-form').hide();
                $('span#loading-icon').hide();
                $('.create-end-document-btn').show();
            }
        });
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
            
        if (selectedValue != undefined) {
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
                        window.location.href = "https://jiserp.com/checks";
                    }
                },
                error: function() {
                    alert('Error al guardar los datos');
                }
            });
        } else {
            alert('Debes ingresar la respuesta');
            $('span#loading-icon_' + rowId).hide();
            $('.guardar-btn').show();
        }
    });

    $('.sigPad').signaturePad({drawOnly:true});

    $("#regime_afp").hide();
    $(".progressive_vacation_date").hide();

    $('body').on('mousemove', function(event) {
        var regime_id = $("#regime_id").val();
        var progressive_vacation_status_id = $("#progressive_vacation_status_id").val();

        if(regime_id == 1) {
            $("#regime_afp").show();
        } else {
            $("#regime_afp").hide();
        }

        if(progressive_vacation_status_id == 1) {
            $(".progressive_vacation_date").show();
        } else {
            $(".progressive_vacation_date").hide();
        }
    });

    $('body').on('mousemove', function(event) {
        var health_id = $("#health_id").val();

        if (health_id != '') {
            if(health_id != 2) {
                $("#health_company").show();
            } else {
                $("#health_company").hide();
            }
        } else {
            $("#health_company").hide();
        }
    });

    var api = $('.sigPad').signaturePad();

    $('#save-button').click(function(){
        var dataUrl = api.getSignatureImage();

        $('#save-button').hide()
        $('span#loading-icon-signature').show();

        var rut =  $('#rut').val()

        rut = rut.split('-')
        rut = rut[0]

        $.ajax({
            type: "POST",
            url: '/signature/store',
            data: { signature: dataUrl },
            success: function(response) {
                $('#save-button').show()
                $('span#loading-icon-signature').hide();
                window.location.href = 'https://jiserp.com/human_resources/personal_data/' + rut;
            }
        });
    });

    $('#progressive_vacation_status_id').change(function() {
        var id = $(this).val()
        if(id == 1) {
            $(".progressive_vacation_date").show();
        } else {
            $(".progressive_vacation_date").hide();
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

        var voluntary_indemnity = $(this).val().replace(/\./g, '');
        var indemnity_years_service = $("#indemnity_years_service").val().replace(/\./g, '');
        var substitute_compensation = $("#substitute_compensation").val().replace(/\./g, '');
        var fertility_proportional = $("#fertility_proportional").val().replace(/\./g, '');

        $(".voluntary_indemnity").val(voluntary_indemnity)

        total = parseInt(voluntary_indemnity) + parseInt(indemnity_years_service) + parseInt(substitute_compensation) + parseInt(fertility_proportional)

        $("#total").val(total)
    });

    $("#indemnity_years_service").change(function() {
        var total

        var voluntary_indemnity = $("#voluntary_indemnity").val().replace(/\./g, '');
        var indemnity_years_service = $(this).val().replace(/\./g, '');
        var substitute_compensation = $("#substitute_compensation").val().replace(/\./g, '');
        var fertility_proportional = $("#fertility_proportional").val().replace(/\./g, '');

        $("#indemnity_years_service").val(indemnity_years_service) 

        total = parseInt(voluntary_indemnity) + parseInt(indemnity_years_service) + parseInt(substitute_compensation) + parseInt(fertility_proportional)

        $("#total").val(total)
    });

    $("#substitute_compensation").change(function() {
        var total

        var voluntary_indemnity = $("#voluntary_indemnity").val().replace(/\./g, '');
        var indemnity_years_service = $("#indemnity_years_service").val().replace(/\./g, '');
        var substitute_compensation = $(this).val().replace(/\./g, '');
        var fertility_proportional = $("#fertility_proportional").val().replace(/\./g, '');

        $("#substitute_compensation").val(substitute_compensation) 

        total = parseInt(voluntary_indemnity) + parseInt(indemnity_years_service) + parseInt(substitute_compensation) + parseInt(fertility_proportional)

        $("#total").val(total)
    });

    $("#fertility_proportional").change(function() {
        var total

        var voluntary_indemnity = $("#voluntary_indemnity").val().replace(/\./g, '');
        var indemnity_years_service = $("#indemnity_years_service").val().replace(/\./g, '');
        var substitute_compensation = $("#substitute_compensation").val().replace(/\./g, '');
        var fertility_proportional = $(this).val().replace(/\./g, '');

        $("#fertility_proportional").val(fertility_proportional) 

        total = parseInt(voluntary_indemnity) + parseInt(indemnity_years_service) + parseInt(substitute_compensation) + parseInt(fertility_proportional)

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

    $('.rut').mask('99999999-Z', {
        translation: {
            'Z': {
                pattern: /[0-9kK]/,
                optional: false
            }
        }
    });
    
    $('.money_value').mask('000.000.000.000', {reverse: true, autoclear: false});

    $('#branch_office_id').change(function() {
        $.ajax({
            url: '/branch_offices/employees/' + $(this).val(),
            type: 'GET',
            success: function(data) {
                $('#employee_id').empty();
                $('#employee_id').append('<option value="">- Seleccionar -</option>');

                data = JSON.parse(data)
                for (var i = 0; i < data.length; ++i) {
                    $('<option value="'+data[i].rut+'">'+data[i].nickname+'</option>').appendTo('#employee_id');
                }
            }
        });
    });

    $('#group_id').change(function() {
        $.ajax({
            url: '/turns/types/' + $('#employee_id').val() + '/' + $(this).val(),
            type: 'GET',
            success: function(data) {
                $(".select_turn").removeAttr('style');
                $(".alert-turn-form").attr('style', 'display:none');

                data = JSON.parse(data)
                $('#turns').empty();

                for (var i = 0; i < data.length; ++i) {
                    $('<div duration="'+ data[i].group_day_id +'" class="fc-event fc-h-event fc-daygrid-event fc-daygrid-block-event"><div class="fc-event-main"><center>Id: '+ data[i].id +' - Horario: '+ data[i].turn +'. Días: '+ data[i].group_day_id +'x' + data[i].free_day_group_id + '</center></div></div>').appendTo('#turns');
                }
            }
        });
    });

    $('ul.index a').on('click', function(event) {
        if (this.hash !== '') {
          event.preventDefault();
          var hash = this.hash;
          $('html, body').animate({
            scrollTop: $(hash).offset().top
          }, 800, function() {
            window.location.hash = hash;
          });
        }
    });
});