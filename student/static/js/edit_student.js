$(document).ready(function()
{
	$(".data_grp").hover(function()
	{
		$(this).find(".edit_btn").show();
	},
	function()
	{
		$(this).find(".edit_btn").hide();			
	});
	$(document).on("click",".edit_btn",function()
	{
		$(this).parents(".data_grp").find(".data_div").find(".data").attr("contenteditable",true);
		$(this).parents(".data_grp").find(".data_div").find(".data").focus();
		content = $(this).parents(".data_grp").find(".data_div").find(".data");
		content.text(content.text());
	});
	$(".data").blur(function()
	{
		var rel = $(this).parents(".data_grp").attr('rel');
		var data = $(this).text();
		var caller = $(this);
		var csrf = $("#csrf_token").find("input").val();
		$.ajax
		({
			type: "POST",
			url: "student/update_cell/",
			data: { cell: rel, data: data, csrfmiddlewaretoken: csrf},
			success: function()
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
	$(".batch_edit").change(function()
	{
		var rel = $(this).parents(".data_grp").attr('rel');
		var data = $(this).val();
		var caller = $(this);
		var csrf = $("#csrf_token").find("input").val();
		$.ajax
		({
			type: "POST",
			url: "student/update_cell/",
			data: { cell: rel, data: data, csrfmiddlewaretoken: csrf},
			success: function()
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