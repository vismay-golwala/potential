$(document).ready(function()
{
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
        	}
        });
    });
    alert('ck');
    $("#attendance_link").trigger("click");
});