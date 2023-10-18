from django.shortcuts import render, redirect, get_object_or_404
from .models import JobPosting
from .forms import JobPostingForm
from django.db import connection

def create_job_posting(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job_posting = form.save(commit=False)

            job_posting.save()
            return redirect('job_postings')
    else:
        form = JobPostingForm()
    
    return render(request, 'create_job.html', {'form': form})

def job_postings(request):
    job_postings = JobPosting.objects.all()
    return render(request,'jobPosting.html',{'job_postings': job_postings})

def job_posting_detail(request, job_posting_id):
    job_posting = get_object_or_404(JobPosting, pk=job_posting_id)
    return render(request, 'job_posting_detail.html', {'job_posting': job_posting})

def custom_job_posting(request):
    custom_sql_query = """
    SELECT id, title, description, created_at FROM jobs_jobposting ORDER BY created_at DESC;"""

    with connection.cursor() as cursor:
        cursor.execute(custom_sql_query)
        columns = [col[0] for col in cursor.description]  
        job_postings = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return render(request, 'custom_job_postings.html', {'job_postings': job_postings})

def add_salary(request):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE jobs_jobposting SET salary = salary * 1.10")

    return redirect('job_postings')

def dec_salary(request):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE jobs_jobposting SET salary = salary - (salary * 0.10)")

    return redirect('job_postings')

def delete_job_posting(request, job_posting_id):
    job_posting = get_object_or_404(JobPosting, pk=job_posting_id)
    
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM jobs_jobposting WHERE id = %s", [job_posting_id])
        
        return redirect('job_postings')
    
    return render(request, 'delete_job_posting.html', {'job_posting': job_posting})