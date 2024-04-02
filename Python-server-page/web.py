from flask import Flask, render_template

app = Flask(__name__)

# Define a route to render the template with dynamic data
@app.route('/')
def index():
   data = {
    'name': 'Brandon Johnson',
    'titles': ['Designer', 'Developer', 'Freelancer', 'Photographer'],
    'social_links': {
        'twitter': '#',
        'facebook': '#',
        'instagram': '#',
        'google_plus': '#',
        'linkedin': '#'
    },
    'description':{
        'facts_description': 'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'skills_description': 'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'services_description': 'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.'


        },
    'about': {
        'about_description': 'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'title': 'UI/UX Designer & Web Developer.',
        'italic_text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        'birthday': '1 May 1995',
        'website': 'www.example.com',
        'phone': '+123 456 7890',
        'city': 'New York, USA',
        'age': '30',
        'degree': 'Master',
        'email': 'email@example.com',
        'freelance': 'Available',
        'additional_text': 'Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.'
    },
    'facts': {
        'happy_clients': 232,
        'projects': 521,
        'hours_of_support': 1463,
        'awards': 25
    },
    'skills': [
        {'name': 'HTML', 'value': 100},
        {'name': 'CSS', 'value': 90},
        {'name': 'JavaScript', 'value': 75},
        {'name': 'PHP', 'value': 80},
        {'name': 'WordPress/CMS', 'value': 90},
        {'name': 'Photoshop', 'value': 55},
        {'name': 'Android', 'value': 75},
    ],
        'resume': {
        'title': 'Resume',
        'description': 'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'sections': [
            {
                'title': 'Summary',
                'items': [
                    {
                        'name': 'Brandon Johnson',
                        'description': 'Innovative and deadline-driven Graphic Designer with 3+ years of experience designing and developing user-centered digital/print marketing material from initial concept to final, polished deliverable.',
                        'address': 'Portland par 127,Orlando, FL',
                        'phone': '(123) 456-7891',
                        'email': 'alice.barkley@example.com'
                    }
                ]
            },
            {
                'title': 'Education',
                'items': [
                    {
                        'degree': 'Master of Fine Arts & Graphic Design',
                        'duration': '2015 - 2016',
                        'institution': 'Rochester Institute of Technology, Rochester, NY',
                        'description': 'Qui deserunt veniam. Et sed aliquam labore tempore sed quisquam iusto autem sit. Ea vero voluptatum qui ut dignissimos deleniti nerada porti sand markend'
                    },
                    {
                        'degree': 'Bachelor of Fine Arts & Graphic Design',
                        'duration': '2010 - 2014',
                        'institution': 'Rochester Institute of Technology, Rochester, NY',
                        'description': 'Quia nobis sequi est occaecati aut. Repudiandae et iusto quae reiciendis et quis Eius vel ratione eius unde vitae rerum voluptates asperiores voluptatem Earum molestiae consequatur neque etlon sader mart dila'
                    }
                ]
            },
            {
                'title': 'Professional Experience',
                'items': [
                    {
                        'title': 'Senior graphic design specialist',
                        'duration': '2019 - Present',
                        'company': 'Experion, New York, NY',
                        'responsibilities': [
                            'Lead in the design, development, and implementation of the graphic, layout, and production communication materials',
                            'Delegate tasks to the 7 members of the design team and provide counsel on all aspects of the project.',
                            'Supervise the assessment of all graphic materials in order to ensure quality and accuracy of the design',
                            'Oversee the efficient use of production project budgets ranging from $2,000 - $25,000'
                        ]
                    },
                    {
                        'title': 'Graphic design specialist',
                        'duration': '2017 - 2018',
                        'company': 'Stepping Stone Advertising, New York, NY',
                        'responsibilities': [
                            'Developed numerous marketing programs (logos, brochures,infographics, presentations, and advertisements).',
                            'Managed up to 5 projects or tasks at a given time while under pressure',
                            'Recommended and consulted with clients on the most appropriate graphic design',
                            'Created 4+ design presentations and proposals a month for clients and account managers'
                        ]
                    }
                ]
            }
        ]
    },

    'portfolio': {
        'title': 'Portfolio',
        'description': 'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'categories': [
            {
                'name': 'App',
                'items': [
                    {
                        'title': 'App 1',
                        'image': 'assets/img/portfolio/portfolio-1.jpg'
                    },
                    {
                        'title': 'App 2',
                        'image': 'assets/img/portfolio/portfolio-3.jpg'
                    },
                    {
                        'title': 'App 3',
                        'image': 'assets/img/portfolio/portfolio-6.jpg'
                    }
                ]
            },
            {
                'name': 'Web',
                'items': [
                    {
                        'title': 'Web 3',
                        'image': 'assets/img/portfolio/portfolio-2.jpg'
                    },
                    {
                        'title': 'Web 2',
                        'image': 'assets/img/portfolio/portfolio-5.jpg'
                    },
                    {
                        'title': 'Web 3',
                        'image': 'assets/img/portfolio/portfolio-9.jpg'
                    }
                ]
            },
            {
                'name': 'Card',
                'items': [
                    {
                        'title': 'Card 2',
                        'image': 'assets/img/portfolio/portfolio-4.jpg'
                    },
                    {
                        'title': 'Card 1',
                        'image': 'assets/img/portfolio/portfolio-7.jpg'
                    },
                    {
                        'title': 'Card 3',
                        'image': 'assets/img/portfolio/portfolio-8.jpg'
                    }
                ]
            }
        ]
    },
     'services': [
        {'title': 'Lorem Ipsum', 'description': 'Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi'},
        {'title': 'Sed Perspiciatis', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore'},
        {'title': 'Magni Dolores', 'description': 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia'},
        {'title': 'Nemo Enim', 'description': 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis'},
        {'title': 'Dele Cardo', 'description': 'Quis consequatur saepe eligendi voluptatem consequatur dolor consequuntur'},
        {'title': 'Divera Don', 'description': 'Modi nostrum vel laborum. Porro fugit error sit minus sapiente sit aspernatur'}
    ],
     'contact': {
        'location': 'A108 Adam Street, New York, NY 535022',
        'email': 'info@example.com',
        'phone': '+1 5589 55488 55'
    },
     'footer': {
        'name': 'Udaya Johnson',
        'description': 'Et aut eum quis fuga eos sunt ipsa nihil. Labore corporis magni eligendi fuga maxime saepe commodi placeat.',
        'social_links': {
            'twitter': '#',
            'facebook': '#',
            'instagram': '#',
            'google_plus': '#',
            'linkedin': '#'
        },
        'credits': 'Designed by <a href="https://bootstrapmade.com/">BootstrapMade</a>'
    }
    }

   return render_template('index2.html', data=data)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5050)
