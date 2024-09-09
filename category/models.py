from django.db import models


class BaseCategory(models.Model):
    name = models.CharField(max_length=100)
    parent = 'None'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('BaseCategory', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    sub_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                   related_name='sub_categories')

    def __str__(self):
        return f'{self.name}'

    def get_ancestors(self):
        """
        Returns a list of ancestors for this category, starting from the root.
        """
        ancestors = []
        category = self
        print()
        print(type(self.parent.name), self.parent, self.parent.name)
        print()
        while category.parent:
            ancestors.insert(0, category.parent)
            print(f'\ncategory self: {category}')
            category = category.parent
            if category:
                print(f'category in break: {category}')

                break
            print(f'category: {category}')
        return ancestors

    def get_descendants(self):
        """
        Returns a list of descendants for this category.
        """
        descendants = []
        children = self.children.all()
        for child in children:
            descendants.append(child)
            descendants.extend(child.get_descendants())
        return descendants

    class Meta:
        ordering = ['name']




"""
categories = {
    "داستانی": "Fiction",
    "غیر داستانی": "Non-fiction",
    "علمی": "Science",
    "تاریخی": "History",
    "جامعه‌شناسی": "Sociology",
    "مذهبی": "Religious",
    "فلسفی": "Philosophy",
    "آموزشی": "Educational",
    "هنری": "Art",
    "زندگی‌نامه": "Biography",
    "کودک و نوجوان": "Children and Young Adult"
}

categories_descriptions = {
    "داستانی": "کتاب‌هایی که داستان‌های تخیلی یا واقع‌گرا را روایت می‌کنند، از جمله رمان‌ها و داستان‌های کوتاه.",
    "غیر داستانی": "کتاب‌هایی که بر مبنای واقعیت‌ها نوشته شده‌اند و به تحلیل یا توضیح مسائل واقعی می‌پردازند.",
    "علمی": "کتاب‌هایی که به بررسی و توضیح علوم طبیعی، فیزیکی و ریاضی می‌پردازند.",
    "تاریخی": "کتاب‌هایی که به مرور و بررسی وقایع تاریخی، زندگی‌نامه‌ها و تحلیل‌های تاریخی اختصاص دارند.",
    "جامعه‌شناسی": "کتاب‌هایی که به مطالعه و تحلیل ساختارها و فرآیندهای اجتماعی، فرهنگی و رفتاری می‌پردازند.",
    "مذهبی": "کتاب‌هایی که به موضوعات دینی، معنوی و مذهبی پرداخته و آموزه‌های مختلف دینی را بررسی می‌کنند.",
    "فلسفی": "کتاب‌هایی که به بررسی مسائل بنیادین وجود، دانش، اخلاق و اندیشه‌های فلسفی اختصاص دارند.",
    "آموزشی": "کتاب‌هایی که برای آموزش و یادگیری موضوعات مختلف طراحی شده‌اند، از جمله کتاب‌های درسی و راهنما.",
    "هنری": "کتاب‌هایی که به موضوعات هنرهای تجسمی، موسیقی، ادبیات و دیگر شاخه‌های هنر اختصاص دارند.",
    "زندگی‌نامه": "کتاب‌هایی که زندگی‌نامه‌ها و خاطرات افراد را روایت می‌کنند و به شرح تجربیات و دستاوردهای آنها می‌پردازند.",
    "کودک و نوجوان": "کتاب‌هایی که مخصوص کودکان و نوجوانان نوشته شده و به آموزش، سرگرمی و پرورش خلاقیت آنها کمک می‌کنند."
}





"""










