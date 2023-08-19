from source_code.Interface import *

if __name__ == '__main__':
    Authy()
    if os.path.exists('User/Auth_token.csv'):
        
        with gr.Blocks() as demo:
            gr.Markdown("Steam Multi-TCS information")
            with gr.Tab("Information about one Game"):
                steam_game_interface.render()
                image_interface.render()
            with gr.Tab("Database creation"):
                    database_interface.render()
                    database_interface2.render()
            with gr.Tab("User Information"):
                    user_information_interface.render()
                    user_information_interface2.render()
        
        webbrowser.open('http://localhost:7860')
        demo.launch()
