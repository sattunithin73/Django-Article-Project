from django.shortcuts import render

article_data = [
    {
        'id': 1,
        'Title':'This is all about India',
        'Desc':'India is a diverse country located in South Asia and is known for its rich culture, traditions, and long history. It is the world’s largest democracy and has a population with many different languages, religions, and customs. India has made significant progress in areas like technology, space research, education, and industry. It is also famous for historical monuments such as the Taj Mahal and many other cultural landmarks.',
        'image':'https://upload.wikimedia.org/wikipedia/commons/1/1d/Taj_Mahal_%28Edited%29.jpeg'
    },
    {
        'id': 2,
        'Title':'This is all about Hyderabad',
        'Desc':'Hyderabad is the capital city of Telangana and one of the major IT and business centers in India. The city is well known for its historical monument, the Charminar, which represents its rich history and culture. Hyderabad is also famous for its traditional dish, Hyderabadi Biryani. With the growth of many technology companies and IT parks, the city is often called “Cyberabad.”',
        'image':'https://aurorealty.com/blog/wp-content/uploads/2025/02/view-historic-building-against-blue-sky.jpg'
    },
    {
        'id': 3,
        'Title':'This is all about Chennai',
        'Desc':'Chennai is the capital of Tamil Nadu and one of the important metropolitan cities in India. It is a major center for the automobile industry and manufacturing sector. Chennai is also known for its cultural heritage, classical music, and traditional dance forms like Bharatanatyam. One of its most famous attractions is the beautiful Marina Beach, which is one of the longest urban beaches in the world.',
        'image':'https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Chennai_Central.jpg/330px-Chennai_Central.jpg'
    },
    {
        'id': 4,
        'Title':'This is all about Bangalore',
        'Desc':'Bengaluru is the capital of Karnataka and is widely known as the “Silicon Valley of India.” The city is a major hub for information technology, startups, and innovation. Many global tech companies have offices in Bengaluru, making it one of the leading technology centers in the country. The city is also known for its pleasant climate and beautiful parks such as Lalbagh Botanical Garden.',
        'image':'https://s7ap1.scene7.com/is/image/incredibleindia/vidhana-soudha-bangalore-karnataka-hero?qlt=82&ts=1742199603184'
    },
    {
        'id': 5,
        'Title':'This is all about Mumbai',
        'Desc':'Mumbai is the financial capital of India and one of the most populated cities in the country. It is home to major financial institutions like the Bombay Stock Exchange. Mumbai is also famous for being the center of the Indian film industry, known as Bollywood. Popular tourist attractions in the city include the historic Gateway of India and the scenic Marine Drive.',
        'image':'https://cdn.britannica.com/26/84526-050-45452C37/Gateway-monument-India-entrance-Mumbai-Harbour-coast.jpg'
    }
]

# Create your views here.
def home(request):
    context ={'data':article_data}
    return render(request,'home.html',context)

def news(request):
    return render(request,'news.html')

def events(request):
    return render(request,'events.html')

def about(request):
    return render(request,'about.html')

def read(request,id):
    print(id)
    for i in article_data:
        print(i['id'])
        if i['id'] == id:
            context = i 
            print(context)
    return render(request,'read.html',context)