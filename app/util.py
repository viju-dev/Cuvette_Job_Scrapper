# app/utils.py

# def format_data(data):
#     # Example formatting logic (replace with your own)
#     formatted_data = {'title': data['title'].strip()}
#     return formatted_data


def format_data(job):
    """
    Format job data.

    Args:
        job (dict): Dictionary containing job details.

    Returns:
        dict: Formatted job data.
    """
    formatted_job = {
        'title': job.get('title', ''),
        'company': job.get('company', ''),
        'location': job.get('location', ''),
        'skills': job.get('skills', ''),
        'link': job.get('link', '')
    }
    return formatted_job