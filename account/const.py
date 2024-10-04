class AccountConst:
    ADMIN_TYPE_CHOICES = [
        ('content_admin', 'Content Admin'),
        ('user_admin', 'User Admin'),
        ('tech_admin', 'Tech Admin'),
        ('financial_admin', 'Financial Admin'),
    ]
    USER_TYPE_CHOICES = [
        ('user', 'User'),
        ('publisher', 'Publisher'),
        ('admin', 'Admin'),
    ]
    SEX_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('N', 'Rather not say'),
    ]
