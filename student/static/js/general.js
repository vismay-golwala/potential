$(document).ready(function()
{
    $("#loader_div").remove();
    $(".select").select2
    ({
        allowClear: true
    });
	$(".sidebar-menu li a").click(function(e)
    {
        e.preventDefault();
        url = $(this).attr('ref');

        if(url=="" || url==undefined || url==null)
            return;
        $.ajax
        ({
        	type: "GET",
        	url: url,
        	data: {},
        	success: function(response)
        	{
        		$("#content_div").html(response);
                $(".select").select2
                ({
                    allowClear: true
                });
                $('input[type="date"]').val(new Date().toJSON().slice(0,10));
                $('input[type="month"]').val(new Date().toJSON().slice(0,7));
        	}
        });
    });
    $("#attendance_link").trigger('click');
});