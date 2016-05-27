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

        $(".sidebar-menu li a").removeClass("current_link")
        $(this).addClass("current_link");
        
        $("#link_title").text($(this).text());
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
                if($("#id_date").length>0)
                {
                    $("#id_date").attr('type','date');
                }
                $('input[type="date"]').val(new Date().toJSON().slice(0,10));
                $('input[type="month"]').val(new Date().toJSON().slice(0,7));
        	}
        });
    });
    setTimeout(function()
        {
            $("#attendance_link").parents(".treeview-menu").prev().trigger('click');
            $("#attendance_link").trigger('click');
        },100);
});