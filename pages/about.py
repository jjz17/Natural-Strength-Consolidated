import streamlit as st


def app():
    about = st.container()

    with about:
        st.header('About Us')
        st.markdown('**In the advent of social media, impressive lifts are around everywhere we look. However, '
                    'not all of what we see is performed by natural athletes. We can easily mistake enhanced '
                    'performances as those performed  natural lifters, which can leave many of us discouraged in our '
                    'own strength journeys. That\'s why we have created this web '
                    'application to update you on what numbers World Class Natural Lifters are producing, as well '
                    'as tools for you to set informed goals in order to build your own natural strength**')
        st.markdown('**USA Powerlifting (USAPL) is an organization which is known for their promotion of the sport of '
                    'powerlifting and their unwavering commitment to providing fair, drug-tested powerlifting '
                    'competitions. On their website, their mission statement is clear: \"It is the mission of USA '
                    'Powerlifting to provide powerlifting competitions of uniform high quality which are drug tested '
                    'and available to all athletes who meet the criteria for membership throughout the United S'
                    'tates.\"**')
        st.markdown('**This is why we are sure that choosing to use their competition data to accurately gauge the '
                    'peak performance of natural lifters, as well as to generate our own personal strength goals, is '
                    'the best choice for our users and ourselves.**')
        st.text('Note: we are not affiliated with USAPL')
        st.image('https://www.usapowerlifting.com/wp-content/uploads/2021/04/USA-Powerlifting-Logo.svg')
        st.video('https://youtu.be/zBlGzXXtQYs')
