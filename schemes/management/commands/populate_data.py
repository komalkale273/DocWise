import datetime
from django.core.management.base import BaseCommand
from schemes.models import Schemes, Notification
from documents.models import Documents, ServiceCenter

class Command(BaseCommand):
    help = 'Populates the database with realistic Indian schemes, documents, and service centers'

    def handle(self, *args, **kwargs):
        # Clear existing data to prevent duplicates on rebuild
        Notification.objects.all().delete()
        Schemes.objects.all().delete()
        Documents.objects.all().delete()
        ServiceCenter.objects.all().delete()

        self.stdout.write("Cleared existing data.")

        # --- Populate Documents ---
        docs = {}
        
        # 1. Birth Certificate
        docs['birth_cert'] = Documents.objects.create(
            title_en="Birth Certificate",
            title_hi="जन्म प्रमाण पत्र",
            title_mr="जन्म दाखला",
            description_en="Official document recording the birth of a child, essential for identity verification and admission.",
            description_hi="बच्चे के जन्म को प्रमाणित करने वाला आधिकारिक दस्तावेज़, पहचान और स्कूल प्रवेश के लिए आवश्यक।",
            description_mr="मुलाच्या जन्माची नोंदणी करणारे अधिकृत दस्तऐवज, ओळख आणि शाळेत प्रवेशासाठी आवश्यक.",
            category="Birth & Childhood",
            preferred_age=0,
            required_for_application=True,
            how_to_get_document_en="Apply online at the municipal corporation portal or visit the local ward office within 21 days of birth.",
            how_to_get_document_hi="जन्म के 21 दिनों के भीतर नगर निगम पोर्टल पर ऑनलाइन आवेदन करें या स्थानीय वार्ड कार्यालय में जाएं।",
            how_to_get_document_mr="जन्माच्या २१ दिवसांच्या आत महानगरपालिकेच्या पोर्टलवर ऑनलाईन अर्ज करा किंवा स्थानिक प्रभाग कार्यालयात भेट द्या.",
            issuing_authority="Municipal Corporation / Registrar of Births",
            min_age=0,
            max_age=5,
            state="All",
            caste="All",
            profession="None"
        )

        # 2. Aadhaar Card
        docs['aadhaar'] = Documents.objects.create(
            title_en="Aadhaar Card",
            title_hi="आधार कार्ड",
            title_mr="आधार कार्ड",
            description_en="12-digit unique identity number issued by UIDAI, serving as proof of identity and address across India.",
            description_hi="UIDAI द्वारा जारी 12-अंकीय विशिष्ट पहचान संख्या, पूरे भारत में पहचान और पते के प्रमाण के रूप में मान्य।",
            description_mr="UIDAI द्वारे जारी केलेला १२-अंकी युनिक ओळख क्रमांक, जो संपूर्ण भारतात ओळख आणि पत्त्याचा पुरावा म्हणून काम करतो.",
            category="Identity",
            preferred_age=5,
            required_for_application=True,
            how_to_get_document_en="Book appointment online at UIDAI website and visit the nearest Aadhaar Seva Kendra for biometrics.",
            how_to_get_document_hi="UIDAI वेबसाइट पर ऑनलाइन अपॉइंटमेंट बुक करें और बायोमेट्रिक्स के लिए निकटतम आधार सेवा केंद्र पर जाएं।",
            how_to_get_document_mr="UIDAI च्या वेबसाइटवर ऑनलाईन अपॉइंटमेंट बुक करा आणि बायोमेट्रिक्ससाठी जवळच्या आधार सेवा केंद्राला भेट द्या.",
            issuing_authority="UIDAI (Unique Identification Authority of India)",
            min_age=0,
            max_age=100,
            state="All",
            caste="All",
            profession="All"
        )

        # 3. PAN Card
        docs['pan'] = Documents.objects.create(
            title_en="PAN Card (Permanent Account Number)",
            title_hi="पैन कार्ड (स्थायी खाता संख्या)",
            title_mr="पॅन कार्ड (कायमस्वरूपी खाते क्रमांक)",
            description_en="Ten-digit alphanumeric identifier issued by the Income Tax Department for financial and tax-related transactions.",
            description_hi="आयकर विभाग द्वारा जारी दस-अंकीय अल्फ़ान्यूमेरिक पहचान संख्या, वित्तीय और कर-संबंधी लेनदेन के लिए आवश्यक।",
            description_mr="वित्तीय आणि कर-संबंधित व्यवहारांसाठी आयकर विभागाने जारी केलेला दहा-अंकी अक्षरी-अंकी ओळख क्रमांक.",
            category="Finance & Identity",
            preferred_age=18,
            required_for_application=True,
            how_to_get_document_en="Apply online on NSDL/UTIITSL portals, submit proof of identity, and receive physical card within 15 days.",
            how_to_get_document_hi="NSDL/UTIITSL पोर्टल पर ऑनलाइन आवेदन करें, पहचान का प्रमाण जमा करें, और 15 दिनों में कार्ड प्राप्त करें।",
            how_to_get_document_mr="NSDL/UTIITSL पोर्टलवर ऑनलाईन अर्ज करा, ओळखीचा पुरावा सबमिट करा आणि १५ दिवसांच्या आत पॅन कार्ड मिळवा.",
            issuing_authority="Income Tax Department of India",
            min_age=18,
            max_age=100,
            state="All",
            caste="All",
            profession="All"
        )

        # 4. Driving License
        docs['driving_license'] = Documents.objects.create(
            title_en="Driving License",
            title_hi="ड्राइविंग लाइसेंस",
            title_mr="वाहन परवाना (ड्रायव्हिंग लायसन्स)",
            description_en="Official document permitting an individual to operate motorized vehicles on public roads.",
            description_hi="सार्वजनिक सड़कों पर मोटर चालित वाहन चलाने की अनुमति देने वाला आधिकारिक दस्तावेज़।",
            description_mr="सार्वजनिक रस्त्यावर मोटार वाहने चालवण्याची परवानगी देणारे अधिकृत दस्तऐवज.",
            category="Transport",
            preferred_age=18,
            required_for_application=False,
            how_to_get_document_en="Apply for a Learner's License online on Sarathi Parivahan, pass test, and apply for a Permanent License after 30 days.",
            how_to_get_document_hi="सारथी परिवहन पर ऑनलाइन लर्नर लाइसेंस के लिए आवेदन करें, परीक्षा पास करें, और 30 दिनों के बाद स्थायी लाइसेंस के लिए आवेदन करें।",
            how_to_get_document_mr="सारथी परिवहनवर ऑनलाईन शिकाऊ परवान्यासाठी अर्ज करा, चाचणी उत्तीर्ण व्हा आणि ३० दिवसांनंतर कायमस्वरूपी परवान्यासाठी अर्ज करा.",
            issuing_authority="Regional Transport Office (RTO)",
            min_age=18,
            max_age=75,
            state="All",
            caste="All",
            profession="All"
        )

        # 5. Caste Certificate
        docs['caste_cert'] = Documents.objects.create(
            title_en="Caste Certificate",
            title_hi="जाति प्रमाण पत्र",
            title_mr="जातीचे प्रमाणपत्र",
            description_en="Document proving an individual belongs to a particular caste, required to claim reservation benefits.",
            description_hi="विशेष जाति से संबंधित होने का प्रमाण पत्र, आरक्षण और छात्रवृत्ति का लाभ उठाने के लिए आवश्यक।",
            description_mr="एखादी व्यक्ती विशिष्ट जातीची असल्याचे सिद्ध करणारे दस्तऐवज, आरक्षण आणि इतर लाभांसाठी आवश्यक.",
            category="Identity & Education",
            preferred_age=15,
            required_for_application=True,
            how_to_get_document_en="Apply online on Aaple Sarkar (for Maharashtra) or visit the local Tehsil/SDO office with family lineage proofs.",
            how_to_get_document_hi="आपले सरकार (महाराष्ट्र के लिए) पर ऑनलाइन आवेदन करें या पारिवारिक वंशावली प्रमाणों के साथ स्थानीय तहसील कार्यालय जाएं।",
            how_to_get_document_mr="आपले सरकार (महाराष्ट्रासाठी) पोर्टलवर ऑनलाईन अर्ज करा किंवा कौटुंबिक पुराव्यांसह स्थानिक तहसील कार्यालयाला भेट द्या.",
            issuing_authority="Revenue Department / Tahsildar",
            min_age=5,
            max_age=100,
            state="Maharashtra",
            caste="OBC",
            profession="Student"
        )

        # 6. Income Certificate
        docs['income_cert'] = Documents.objects.create(
            title_en="Income Certificate",
            title_hi="आय प्रमाण पत्र",
            title_mr="उत्पन्नाचा दाखला",
            description_en="Certificate stating the annual family income, required for scholarship and welfare scheme eligibility.",
            description_hi="वार्षिक पारिवारिक आय को प्रमाणित करने वाला प्रमाण पत्र, छात्रवृत्ति और कल्याणकारी योजनाओं की पात्रता के लिए आवश्यक।",
            description_mr="कुटुंबाचे वार्षिक उत्पन्न दर्शविणारे प्रमाणपत्र, शिष्यवृत्ती आणि कल्याणकारी योजनांच्या पात्रतेसाठी आवश्यक.",
            category="Finance & Welfare",
            preferred_age=18,
            required_for_application=True,
            how_to_get_document_en="Apply online on state portal (e.g. Aaple Sarkar) by submitting salary slips, ITR, or declaration forms.",
            how_to_get_document_hi="वेतन पर्ची, आईटीआर या स्व-घोषणा पत्र जमा करके राज्य पोर्टल पर ऑनलाइन आवेदन करें।",
            how_to_get_document_mr="पगार पत्रक, आयटीआर किंवा स्वयं-घोषणापत्र सबमिट करून राज्य पोर्टलवर ऑनलाईन अर्ज करा.",
            issuing_authority="Revenue Department / Tahsildar",
            min_age=15,
            max_age=100,
            state="All",
            caste="All",
            profession="All"
        )

        # 7. Senior Citizen Card
        docs['senior_card'] = Documents.objects.create(
            title_en="Senior Citizen Card",
            title_hi="वरिष्ठ नागरिक कार्ड",
            title_mr="ज्येष्ठ नागरिक ओळखपत्र",
            description_en="Special identity card for citizens aged 60 and above, offering concession benefits in travel, healthcare, and services.",
            description_hi="60 वर्ष और उससे अधिक उम्र के नागरिकों के लिए विशेष पहचान पत्र, यात्रा, स्वास्थ्य सेवा और रियायतें प्रदान करता है।",
            description_mr="६० वर्षे आणि त्याहून अधिक वयाच्या नागरिकांसाठी विशेष ओळखपत्र, जे प्रवास, आरोग्य सेवा आणि सवलतीचे फायदे प्रदान करते.",
            category="Senior Citizens",
            preferred_age=60,
            required_for_application=False,
            how_to_get_document_en="Apply online on the state social welfare department portal or visit local district offices with proof of age.",
            how_to_get_document_hi="राज्य समाज कल्याण विभाग पोर्टल पर ऑनलाइन आवेदन करें या आयु प्रमाण के साथ स्थानीय जिला कार्यालयों में जाएं।",
            how_to_get_document_mr="राज्य समाज कल्याण विभागाच्या पोर्टलवर ऑनलाईन अर्ज करा किंवा वयाच्या पुराव्यासह स्थानिक जिल्हा कार्यालयांना भेट द्या.",
            issuing_authority="Department of Social Justice and Special Assistance",
            min_age=60,
            max_age=100,
            state="All",
            caste="All",
            profession="All"
        )

        self.stdout.write(f"Populated {len(docs)} Documents successfully.")

        # --- Populate Schemes ---
        today = datetime.date.today()
        deadline_date = today + datetime.timedelta(days=45)

        # 1. Sukanya Samriddhi Yojana (SSY)
        ssy = Schemes.objects.create(
            title_en="Sukanya Samriddhi Yojana (SSY)",
            title_hi="सुकन्या समृद्धि योजना (SSY)",
            title_mr="सुकन्या समृद्धी योजना (SSY)",
            description_en="A small deposit scheme for a girl child launched as a part of the 'Beti Bachao Beti Padhao' campaign, offering high interest rates and tax savings.",
            description_hi="बेटी बचाओ बेटी पढ़ाओ अभियान के तहत बालिकाओं के लिए एक छोटी बचत योजना, जो उच्च ब्याज दर और कर बचत प्रदान करती है।",
            description_mr="बालिकांसाठी सुरू करण्यात आलेली एक लहान बचत योजना, जी उच्च व्याजदर आणि कर बचत प्रदान करते.",
            scheme_application_start_date=today,
            deadline_scheme_application=deadline_date,
            age_limit=10, # Applies to girls up to 10
            income_limit=10000000,
            caste="All",
            state="All",
            profession="Student",
            category="newborn_parent", # Life stage Newborn Parent or Child
            deadline=deadline_date,
            scheme_type="government"
        )
        ssy.required_documents.add(docs['birth_cert'], docs['aadhaar'])

        # 2. Post Matric Scholarship for OBC Students
        obc_scholarship = Schemes.objects.create(
            title_en="Post Matric Scholarship for OBC Students",
            title_hi="ओबीसी छात्रों के लिए पोस्ट मैट्रिक छात्रवृत्ति",
            title_mr="इतर मागासवर्गीय विद्यार्थ्यांसाठी मॅट्रिकोत्तर शिष्यवृत्ती",
            description_en="Financial assistance scheme for OBC students pursuing post-matric courses to support their higher education costs.",
            description_hi="उच्च शिक्षा लागत में सहायता के लिए पोस्ट-मैट्रिक पाठ्यक्रम करने वाले ओबीसी छात्रों के लिए वित्तीय सहायता योजना।",
            description_mr="मॅट्रिकोत्तर शिक्षण घेणाऱ्या ओबीसी विद्यार्थ्यांसाठी त्यांच्या उच्च शिक्षणाचा खर्च भागवण्यासाठी आर्थिक सहाय्य योजना.",
            scheme_application_start_date=today,
            deadline_scheme_application=deadline_date,
            age_limit=25,
            income_limit=150000,
            caste="OBC",
            state="Maharashtra",
            profession="Student",
            category="student",
            deadline=deadline_date,
            scheme_type="government"
        )
        obc_scholarship.required_documents.add(docs['aadhaar'], docs['caste_cert'], docs['income_cert'])

        # 3. Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)
        pm_kisan = Schemes.objects.create(
            title_en="Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
            title_hi="प्रधानमंत्री किसान सम्मान निधि (PM-KISAN)",
            title_mr="पंतप्रधान किसान सन्मान निधी (PM-KISAN)",
            description_en="Government initiative that provides up to ₹6,000 per year in three equal installments as income support to all landholding farmer families.",
            description_hi="एक सरकारी पहल जो सभी भूमिधारक किसान परिवारों को आय सहायता के रूप में तीन समान किश्तों में प्रति वर्ष ₹6,000 तक प्रदान करती है।",
            description_mr="एक सरकारी उपक्रम जो सर्व जमीनधारक शेतकरी कुटुंबांना उत्पन्न सहाय्य म्हणून तीन समान हप्त्यांमध्ये वर्षाला ₹६,००० प्रदान करतो.",
            scheme_application_start_date=today,
            deadline_scheme_application=deadline_date,
            age_limit=80,
            income_limit=300000,
            caste="All",
            state="All",
            profession="Farmer",
            category="mid_age",
            deadline=deadline_date,
            scheme_type="government"
        )
        pm_kisan.required_documents.add(docs['aadhaar'], docs['pan'], docs['income_cert'])

        # 4. Atal Pension Yojana (APY)
        apy = Schemes.objects.create(
            title_en="Atal Pension Yojana (APY)",
            title_hi="अटल पेंशन योजना (APY)",
            title_mr="अटल पेन्शन योजना (APY)",
            description_en="Pension scheme targeted at unorganized sector workers, providing a guaranteed minimum pension of ₹1,000 to ₹5,000 per month after age 60.",
            description_hi="असंगठित क्षेत्र के श्रमिकों के लिए पेंशन योजना, जो 60 वर्ष की आयु के बाद ₹1,000 से ₹5,000 प्रति माह की गारंटीकृत न्यूनतम पेंशन प्रदान करती है।",
            description_mr="असंघटित क्षेत्रातील कामगारांसाठी पेन्शन योजना, जी वयाच्या ६० वर्षांनंतर दरमहा ₹१,००० ते ₹५,००० ची हमी पेन्शन प्रदान करते.",
            scheme_application_start_date=today,
            deadline_scheme_application=deadline_date,
            age_limit=40,
            income_limit=500000,
            caste="All",
            state="All",
            profession="Worker",
            category="young_adult",
            deadline=deadline_date,
            scheme_type="government"
        )
        apy.required_documents.add(docs['aadhaar'], docs['pan'])

        # 5. PM Mudra Yojana
        mudra = Schemes.objects.create(
            title_en="Pradhan Mantri Mudra Yojana (PMMY)",
            title_hi="प्रधानमंत्री मुद्रा योजना (PMMY)",
            title_mr="पंतप्रधान मुद्रा योजना (PMMY)",
            description_en="Scheme providing loans up to ₹10 Lakhs to non-corporate, non-farm small/micro enterprises to encourage entrepreneurship and self-employment.",
            description_hi="गैर-कॉर्पोरेट, गैर-कृषि लघु/सूक्ष्म उद्यमों को उद्यमिता और स्वरोजगार को बढ़ावा देने के लिए ₹10 लाख तक का ऋण प्रदान करने वाली योजना।",
            description_mr="उद्योजकता आणि स्वयंरोजगाराला प्रोत्साहन देण्यासाठी बिगर-कॉर्पोरेट, बिगर-शेती लघु/सूक्ष्म उपक्रमांना ₹१० लाखांपर्यंत कर्ज देणारी योजना.",
            scheme_application_start_date=today,
            deadline_scheme_application=deadline_date,
            age_limit=65,
            income_limit=10000000,
            caste="All",
            state="All",
            profession="Business",
            category="mid_age",
            deadline=deadline_date,
            scheme_type="government"
        )
        mudra.required_documents.add(docs['aadhaar'], docs['pan'], docs['income_cert'])

        # 6. PM Vidya Lakshmi Education Loan
        vidya = Schemes.objects.create(
            title_en="PM Vidya Lakshmi Scheme",
            title_hi="पीएम विद्या लक्ष्मी योजना",
            title_mr="पीएम विद्या लक्ष्मी योजना",
            description_en="Single portal for students seeking Education Loans and Scholarships for pursuing higher education in India and abroad.",
            description_hi="भारत और विदेशों में उच्च शिक्षा प्राप्त करने के लिए शिक्षा ऋण और छात्रवृत्ति की तलाश करने वाले छात्रों के लिए एकल पोर्टल।",
            description_mr="भारत आणि परदेशात उच्च शिक्षण घेण्यासाठी शैक्षणिक कर्ज आणि शिष्यवृत्ती शोधणाऱ्या विद्यार्थ्यांसाठी एकल पोर्टल.",
            scheme_application_start_date=today,
            deadline_scheme_application=deadline_date,
            age_limit=30,
            income_limit=800000,
            caste="All",
            state="All",
            profession="Student",
            category="student",
            deadline=deadline_date,
            scheme_type="government"
        )
        vidya.required_documents.add(docs['aadhaar'], docs['income_cert'])

        # 7. Indira Gandhi National Old Age Pension Scheme
        pension = Schemes.objects.create(
            title_en="National Old Age Pension Scheme (IGNOAPS)",
            title_hi="इंदिरा गांधी राष्ट्रीय वृद्धावस्था पेंशन योजना",
            title_mr="इंदिरा गांधी राष्ट्रीय वृद्धापकाळ पेन्शन योजना",
            description_en="Financial assistance scheme for elderly citizens belonging to Below Poverty Line (BPL) households, providing monthly pensions.",
            description_hi="गरीबी रेखा से नीचे (BPL) परिवारों से संबंधित बुजुर्ग नागरिकों के लिए मासिक पेंशन प्रदान करने वाली वित्तीय सहायता योजना।",
            description_mr="दारिद्र्यरेषेखालील (BPL) कुटुंबातील वृद्ध नागरिकांसाठी मासिक पेन्शन प्रदान करणारी आर्थिक सहाय्य योजना.",
            scheme_application_start_date=today,
            deadline_scheme_application=deadline_date,
            age_limit=100,
            income_limit=100000,
            caste="All",
            state="All",
            profession="Any",
            category="senior_citizen",
            deadline=deadline_date,
            scheme_type="government"
        )
        pension.required_documents.add(docs['aadhaar'], docs['senior_card'], docs['income_cert'])

        self.stdout.write("Populated 7 Schemes successfully.")

        # --- Populate Service Centers ---
        centers = [
            ServiceCenter(
                name="Thane Maha e-Seva Kendra (CSC)",
                center_type="csc",
                address="Shop No 4, Sai Krupa Building, Gokhale Road, Naupada",
                city="Thane",
                state="Maharashtra",
                pin_code="400602",
                contact_number="022-25381234",
                timings="9:30 AM - 6:30 PM",
                services_offered="Income Certificate, Caste Certificate, Aadhaar Registration, PAN Card",
                latitude=19.196300,
                longitude=72.973400
            ),
            ServiceCenter(
                name="Mumbai Central UIDAI Aadhaar Seva Kendra",
                center_type="csc",
                address="UIDAI Center, Ground Floor, Trade Centre, Bandra Kurla Complex",
                city="Mumbai",
                state="Maharashtra",
                pin_code="400051",
                contact_number="1947",
                timings="9:00 AM - 6:00 PM",
                services_offered="Aadhaar Card Enrollment, Aadhaar Card Mobile/Address Update, Biometric Update",
                latitude=19.059600,
                longitude=72.872200
            ),
            ServiceCenter(
                name="Regional Transport Office (RTO) Thane",
                center_type="rto",
                address="Near Central Jail, Jail Road, Thane West",
                city="Thane",
                state="Maharashtra",
                pin_code="400601",
                contact_number="022-25442555",
                timings="10:00 AM - 5:30 PM",
                services_offered="Learner's License, Permanent Driving License, Vehicle Registration",
                latitude=19.200100,
                longitude=72.981100
            ),
            ServiceCenter(
                name="Naupada Ward Office & Birth Registrar Office",
                center_type="municipal",
                address="TMC Ward Office, Naupada, Near Hariniwas Circle",
                city="Thane",
                state="Maharashtra",
                pin_code="400602",
                contact_number="022-25401122",
                timings="10:00 AM - 5:00 PM",
                services_offered="Birth Certificate Issuance, Death Certificate, Local Municipality Permits",
                latitude=19.192000,
                longitude=72.969000
            ),
            ServiceCenter(
                name="Thane Head Post Office CSC",
                center_type="post_office",
                address="Station Road, Near Thane Railway Station, Thane West",
                city="Thane",
                state="Maharashtra",
                pin_code="400601",
                contact_number="022-25334444",
                timings="9:00 AM - 5:00 PM",
                services_offered="Aadhaar Enrollment, Speed Post, Sukanya Samriddhi Account Opening, Postal Saving Schemes",
                latitude=19.186000,
                longitude=72.972000
            )
        ]
        
        ServiceCenter.objects.bulk_create(centers)
        self.stdout.write(f"Populated {len(centers)} Service Centers successfully.")
        self.stdout.write(self.style.SUCCESS("Database seeding completed!"))
