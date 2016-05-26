$(document).ready(function()
{
	$(document).on("click","#get_attendance_btn",function()
	{
		var batch = $("#batch").val();
		var attendance_date = $("#attendance_date").val();
		var csrf_token = $("#csrf_token").find("input").val();
		
		if(attendance_date == "" || batch == "")
			return;

		$.ajax
		({
		// Check for batch id instead of standard
			type: "POST",
			url: "student/get_attendance/",
			data: { batch: batch, attendance_date: attendance_date, csrfmiddlewaretoken: csrf_token },
			success: function(response)
			{
				$("#attendance_table").html(response);
			},
			error: function()
			{
				alert("Oops, error occured!");
			}
		})
	});
	$(document).on("click","#view_attendance_btn",function()
	{
		var batch = $("#batch_attendance").val();
		var attendance_month = $("#attendance_month").val();
		var csrf_token = $("#csrf_token").find("input").val();
		
		if(attendance_month == "" || batch == "")
			return;

		$.ajax
		({
		// Check for batch id instead of standard
			type: "POST",
			url: "student/view_attendance/",
			data: { batch: batch, attendance_month: attendance_month, csrfmiddlewaretoken: csrf_token },
			success: function(response)
			{
				$("#view_attendance_table").html(response);
			},
			error: function()
			{
				alert("Oops, error occured!");
			}
		})
	});
});