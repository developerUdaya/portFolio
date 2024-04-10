from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


# Define your navigation items, hero data, about data, resume data, testimonials data, portfolio data, pricing data, contact data, and footer data
# Replace the placeholders with your actual data

nav_links = [
    {"label": "Home", "href": "#hero", "dropdown": False},
    {"label": "About", "href": "#about", "dropdown": False},
    {"label": "Resume", "href": "#resume", "dropdown": False},
    {"label": "Services", "href": "#services", "dropdown": False},
    {"label": "Portfolio", "href": "#portfolio", "dropdown": False},
    {
        "label": "Drop Down",
        "href": "#",
        "dropdown": True,
        "sublinks": [
            {"label": "Drop Down 1", "dropdown": False},
            {
                "label": "Deep Drop Down",
                "dropdown": True,
                "sublinks": [
                    {"label": "Deep Drop Down 1", "dropdown": False},
                    {"label": "Deep Drop Down 2", "dropdown": False},
                    {"label": "Deep Drop Down 3", "dropdown": False},
                    {"label": "Deep Drop Down 4", "dropdown": False},
                    {"label": "Deep Drop Down 5", "dropdown": False},
                ],
            },
            {"label": "Drop Down 2", "dropdown": False},
            {"label": "Drop Down 3", "dropdown": False},
            {"label": "Drop Down 4", "dropdown": False},
        ],
    },
    {"label": "Contact", "href": "#contact", "dropdown": False},
]


hero_data = {"title": "Anita", "subtitle": "I'M A PROFESSIONAL PHOTOGRAPHER IN NEW YORK CITY"}

about_data = {
    'title': 'About Me',
    'description': 'Sit sint consectetur velit quisquam cupiditate impedit suscipit alias',
    'Name': 'Laura Thomson',
    'Website': 'www.example.com',
    'Phone': '+123 456 7890',
    'City': 'New York, USA',
    'Age': 30,
    'Degree': 'Master',
    'Email': 'email@example.com',
    'Freelance': 'Available',
    'Counters': [
        {'icon_class': 'bi bi-emoji-smile', 'icon_color': '#20b38e', 'start': 0, 'end': 232, 'title': 'Happy Clients', 'description': 'consequuntur voluptas nostrum aliquid ipsam architecto ut.'},
        {'icon_class': 'bi bi-journal-richtextr', 'icon_color': '#8a1ac2', 'start': 0, 'end': 521, 'title': 'Projects', 'description': 'adipisci atque cum quia aspernatur totam laudantium et quia dere tan'},
        {'icon_class': 'bi bi-clock', 'icon_color': '#2cbdee', 'start': 0, 'end': 18, 'title': 'Years of experience', 'description': 'aut commodi quaerat modi aliquam nam ducimus aut voluptate non vel'},
        {'icon_class': 'bi bi-award', 'icon_color': '#ffb459', 'start': 0, 'end': 16, 'title': 'Awards', 'description': 'rerum asperiores dolor alias quo reprehenderit eum et nemo pad der'}
    ],
    'Skills': [
        {'name': 'HTML', 'percentage': '100'},
        {'name': 'CSS', 'percentage': '90'},
        {'name': 'JavaScript', 'percentage': '75'}
    ]
}


resume_data = {
            'summary': [
                {'name': 'Alice Barkley'},
                {'description': 'Innovative and deadline-driven Graphic Designer with 3+ years of experience designing and developing user-centered digital/print marketing material from initial concept to final, polished deliverable.'},
                {'address': 'Portland par 127,Orlando, FL'},
                {'phone': '(123) 456-7891'},
                {'email': 'alice.barkley@example.com'}
            ],
            'education': [
                {'degree': 'Master of Fine Arts & Graphic Design', 'year': '2015 - 2016', 'institution': 'Rochester Institute of Technology, Rochester, NY', 'description': 'Qui deserunt veniam. Et sed aliquam labore tempore sed quisquam iusto autem sit. Ea vero voluptatum qui ut dignissimos deleniti nerada porti sand markend'},
                {'degree': 'Bachelor of Fine Arts & Graphic Design', 'year': '2010 - 2014', 'institution': 'Rochester Institute of Technology, Rochester, NY', 'description': 'Quia nobis sequi est occaecati aut. Repudiandae et iusto quae reiciendis et quis Eius vel ratione eius unde vitae rerum voluptates asperiores voluptatem Earum molestiae consequatur neque etlon sader mart dila'}
            ],
            'experience': [
                {'title': 'Senior graphic design specialist', 'year': '2019 - Present', 'company': 'Experion, New York, NY', 'description': 'Lead in the design, development, and implementation of the graphic, layout, and production communication materials', 'responsibilities': ['Lead in the design, development, and implementation of the graphic, layout, and production communication materials', 'Delegate tasks to the 7 members of the design team and provide counsel on all aspects of the project.', 'Supervise the assessment of all graphic materials in order to ensure quality and accuracy of the design', 'Oversee the efficient use of production project budgets ranging from $2,000 - $25,000']},
                {'title': 'Graphic design specialist', 'year': '2017 - 2018', 'company': 'Stepping Stone Advertising, New York, NY', 'description': 'Developed numerous marketing programs (logos, brochures,infographics, presentations, and advertisements).', 'responsibilities': ['Developed numerous marketing programs (logos, brochures,infographics, presentations, and advertisements).', 'Managed up to 5 projects or tasks at a given time while under pressure', 'Recommended and consulted with clients on the most appropriate graphic design', 'Created 4+ design presentations and proposals a month for clients and account managers']}
            ]
        
    }      

services_data=[
            {'icon_class': 'bx bxl-dribbble', 'title': 'Lorem Ipsum', 'description': 'Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident'},
            {'icon_class': 'bx bx-file', 'title': 'Sed ut perspiciatis', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur'},
            {'icon_class': 'bx bx-tachometer', 'title': 'Magni Dolores', 'description': 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'},
            {'icon_class': 'bx bx-world', 'title': 'Nemo Enim', 'description': 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque'}]


testimonials_data = [
    {
        'name': 'Saul Goodman',
        'position': 'Ceo & Founder',
        'image': 'static/img/testimonials/testimonials-1.jpg',
        'quote': 'Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.'
    },
    {
        'name': 'Sara Wilsson',
        'position': 'Designer',
        'image': 'static/img/testimonials/testimonials-2.jpg',
        'quote': 'Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid cillum eram malis quorum velit fore eram velit sunt aliqua noster fugiat irure amet legam anim culpa.'
    },
    {
        'name': 'Jena Karlis',
        'position': 'Store Owner',
        'image': 'static/img/testimonials/testimonials-3.jpg',
        'quote': 'Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam duis minim tempor labore quem eram duis noster aute amet eram fore quis sint minim.'
    },
    {
        'name': 'Matt Brandon',
        'position': 'Freelancer',
        'image': 'static/img/testimonials/testimonials-4.jpg',
        'quote': 'Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat minim velit minim dolor enim duis veniam ipsum anim magna sunt elit fore quem dolore labore illum veniam.'
    },
    {
        'name': 'John Larson',
        'position': 'Entrepreneur',
        'image': 'static/img/testimonials/testimonials-5.jpg',
        'quote': 'Quis quorum aliqua sint quem legam fore sunt eram irure aliqua veniam tempor noster veniam enim culpa labore duis sunt culpa nulla illum cillum fugiat legam esse veniam culpa fore nisi cillum quid.'
    }
]


portfolio_data = [
    {
        'img_src': 'static/img/portfolio/portfolio-1.jpg',
        'title': 'App 1',
        'category': 'App',
        'filter': 'filter-app'
    },
    {
        'img_src': 'static/img/portfolio/portfolio-2.jpg',
        'title': 'Web 3',
        'category': 'Web',
        'filter': 'filter-web'
    },
    {
        'img_src': 'static/img/portfolio/portfolio-3.jpg',
        'title': 'App 2',
        'category': 'App',
        'filter': 'filter-app'
    },
    {
        'img_src': 'static/img/portfolio/portfolio-4.jpg',
        'title': 'Card 2',
        'category': 'Card',
        'filter': 'filter-card'
    },
    {
        'img_src': 'static/img/portfolio/portfolio-5.jpg',
        'title': 'Web 2',
        'category': 'Web',
        'filter': 'filter-web'
    },
    {
        'img_src': 'static/img/portfolio/portfolio-6.jpg',
        'title': 'App 3',
        'category': 'App',
        'filter': 'filter-app'
    },
    {
        'img_src': 'static/img/portfolio/portfolio-7.jpg',
        'title': 'Card 1',
        'category': 'Card',
        'filter': 'filter-card'
    },
    {
        'img_src': 'static/img/portfolio/portfolio-8.jpg',
        'title': 'Card 3',
        'category': 'Card',
        'filter': 'filter-card'
    },
    {
        'img_src': 'static/img/portfolio/portfolio-9.jpg',
        'title': 'Web 3',
        'category': 'Web',
        'filter': 'filter-web'
    }
]


pricing_data = [
    {
        'name': 'Free',
        'price': 0,
        'features': ['Aida dere', 'Nec feugiat nisl', 'Nulla at volutpat dola'],
        'featured': False
    },
    {
        'name': 'Business',
        'price': 19,
        'features': ['Aida dere', 'Nec feugiat nisl', 'Nulla at volutpat dola', 'Pharetra massa'],
        'featured': True
    },
    {
        'name': 'Developer',
        'price': 29,
        'features': ['Aida dere', 'Nec feugiat nisl', 'Nulla at volutpat dola', 'Pharetra massa', 'Massa ultricies mi'],
        'featured': False
    },
    {
        'name': 'Ultimate',
        'price': 49,
        'features': ['Aida dere', 'Nec feugiat nisl', 'Nulla at volutpat dola', 'Pharetra massa', 'Massa ultricies mi'],
        'featured': False
    }
]

contact_data = {"email": "example@example.com", "phone": "+1234567890", "social_profiles": {"facebook": "#", "twitter": "#", "linkedin": "#", "instagram": "#"}}

footer_data = {"name": "Anita", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "social_links": {"facebook": "#", "twitter": "#", "linkedin": "#", "instagram": "#", "google-plus": "#"}}

# Route to render the entire page
@app.route('/')
def index():
    return render_template('index2.html', nav_links=nav_links, hero_data=hero_data, about_data=about_data, resume_data=resume_data,services_data=services_data,testimonials_data=testimonials_data, portfolio_data=portfolio_data, pricing_data=pricing_data, contact_data=contact_data, footer_data=footer_data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
