$(document).ready(function()
{
	$(".content_grp").hover(function()
	{
		$(this).find(".edit_btn").show();
	},
	function()
	{
		$(this).find(".edit_btn").hide();			
	});
	$(document).on("click",".edit_btn",function()
	{
		$(this).parents(".content_grp").find(".content_div").find(".content").attr("contenteditable",true);
		$(this).parents(".content_grp").find(".content_div").find(".content").trigger('click');
		$(this).parents(".content_grp").find(".content_div").find(".content").trigger('click');
		$(this).parents(".content_grp").find(".content_div").find(".content").focus();
	});
	$(".content").blur(function()
	{
		var rel = $(this).parents(".content_grp").attr('rel');
		var content = $(this).text();
		var caller = $(this);
		$.ajax
		({
			type: "POST",
			url: "update_cell.php",
			data: { cell: rel, content: content},
			success: function(response)
			{
				if(response=="false")
					alert("There was some problem updating the data.");
				else
				{
					caller.removeAttr("contenteditable");
				}
			}
		});
	});
});