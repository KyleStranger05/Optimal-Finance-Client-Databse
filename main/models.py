from django.db import models

Months = [
    ('January','January'),
    ('February','February'),
    ('March','March'),
    ('April','April'),
    ('May','May'),
    ('June','June'),
    ('July','July'),
    ('August','August'),
    ('September','September'),
    ('October','October'),
    ('Novemeber','Novemeber'),
    ('December','December')
]

class CompanyClass(models.Model):
    #Company Only Fields
    CompanyName = models.CharField(max_length=50 , blank=False)
    RefNo = models.CharField(max_length=50 , blank=False )
    FinancialYearEnd = models.DateField(auto_now=False, auto_now_add=False, null=False)
    ProvisionalTaxDate1 = models.DateField(auto_now=False, auto_now_add=False) #6 months before Financial Year End
    ProvisionalTaxDate2 = models.DateField(auto_now=False, auto_now_add=False) #Current year end (December 31st of the year the user selects)
    ARMonth = models.DateField(auto_now=False, auto_now_add=False)

    #Shared Fields
    TaxRegNo = models.CharField(max_length=50, blank=False )

    #Address
    StreetName = models.CharField(max_length=50, blank=False )
    StreetNo = models.CharField( max_length=50, blank=False)
    BuildingName = models.CharField(max_length=50, blank=False)
    BuildingNo = models.CharField(max_length=50, blank=False)
    Suburb = models.CharField(max_length=50, blank=False)
    City = models.CharField(max_length=50, blank=False)

    #Contact Details
    ContactPerson = models.CharField( max_length=50, blank=False)
    OfficeNumber = models.CharField(max_length=50, blank=False)
    CellNumber = models.CharField(max_length=50, blank=False)
    EmailAddress = models.CharField(max_length=50, blank=False)

    #Services
    IT14 = models.BooleanField(default=True)
    FinancialStatements = models.BooleanField(default=True)
    IsProvisionalTaxPayer = models.BooleanField(default=True)
    AnnualReturns = models.BooleanField(default=True)

    # CheckList
    isdone_IT14 = models.BooleanField(default=False)
    isdone_FinancialStatements = models.BooleanField(default=False)
    isdone_Provisionals = models.BooleanField(default=False)
    isdone_AnnualReturns = models.BooleanField(default=False)

    def __str__(self):
        return ( self.CompanyName)

class IndividualClass(models.Model):
    #Individual Only Fields
    Surname = models.CharField("Company Name",max_length=50 )
    Name = models.CharField("Company Name",max_length=50 )
    IDNo = models.CharField("Company Name",max_length=11 )
    ProvisionalTaxDate1 = models.DateField(auto_now=False, auto_now_add=False)
    ProvisionalTaxDate2 = models.DateField(auto_now=False, auto_now_add=False)

    # Shared Fields
    TaxRegNo = models.CharField("Tax Registration Number", max_length=50)

    # Address
    StreetName = models.CharField("Street Name", max_length=50)
    StreetNo = models.CharField("Street Number (if applicable)", max_length=50)
    BuildingName = models.CharField("Building Name (if applicable)", max_length=50)
    BuildingNo = models.CharField("Building Number (if applicable)", max_length=50)
    Suburb = models.CharField("Suburb", max_length=50)
    City = models.CharField("City", max_length=50)

    # Contact Details
    ContactPerson = models.CharField("Contact Person", max_length=50)
    CellNumber = models.CharField("Cell Number", max_length=50)
    EmailAddress = models.CharField("E-mailAddress", max_length=50)

    # Services
    IT12 = models.BooleanField(default=True)
    IsProvisionalTaxPayer = models.BooleanField(default=True)

    # CheckList
    isdone_IT12 = models.BooleanField(default=False)
    isdone_Provisionals=  models.BooleanField(default=False)

    def __str__(self):
        return ( self.Surname + ' , ' + self.Name )