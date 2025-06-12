from django.contrib.sitemaps import Sitemap
from companies.models import Job


class JobSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Job.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at
