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
	$(".full_edit_btn").click(function()
	{
		var rel = $(this).attr('rel');
		var csrf = $("#csrf_token").find("input").val();
		$.ajax
		({
			type: "GET",
			url: "student/edit_full_student/"+rel+"/",
			data: { csrfmiddlewaretoken: csrf },
			success: function(response)
			{
				$("#edit_content").html(response);
				$("#edit_content").find("form").attr('action','student/edit_full_student/'+rel+'/');
			}
		});
	});
	$(".delete_btn").click(function()
	{
		var rel = $(this).attr('rel');
		var csrf = $("#csrf_token").find("input").val();
		var caller = $(this).parents(".student_record");
		$.confirm
		({
			title: 'Are you sure?',
			content: "You won't be able to revert this action!" ,
			confirmButton: 'Delete',
    		cancelButton: 'Cancel',
			confirmButtonClass: 'btn-danger',
    		cancelButtonClass: 'btn-info',
    		closeIcon: true,
    		closeIconClass: 'glyphicon glyphicon-remove',
    		theme: 'material',
    		backgroundDismiss: true,
			confirm: function()
			{
				$.ajax
				({
					type: "POST",
					url: "student/delete_student/",
					data: { key: rel, csrfmiddlewaretoken: csrf },
					success: function()
					{
						caller.fadeOut("slow");
					}
				});
			},
			cancel: function()
			{
			    
			}
		});
	});
});