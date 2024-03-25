import api_handler
import html_generator

def main():
    birds_info = api_handler.fetch_birds_data()  
    if birds_info:
        html_generator.generate_html(birds_info)

if __name__ == "__main__":
    main()