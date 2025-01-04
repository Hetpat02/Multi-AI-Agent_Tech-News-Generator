from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer
import streamlit as st
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def clean_header(content):
    # Define the header to remove
    unwanted_start = "AI-Powered Tech News Generator Report"
    unwanted_marker = "The final answer is:"
    
    # Check if the content contains the unwanted header and remove it
    if unwanted_start in content and unwanted_marker in content:
        content = content.split(unwanted_marker, 1)[-1]  # Keep everything after "The final answer is:"

    # Remove Markdown-specific elements
    content = content.replace("```", "")
 
    
    # Strip any leading or trailing whitespace
    return content.strip()


# Streamlit app title
st.title("AI-Powered Tech News Generator")

# Input for topic
topic = st.text_input("Enter a technology topic: ")

# Create Crew instance
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)

# Button to generate the report
if st.button("Generate Report"):
    with st.spinner("Researching and writing... This may take a few minutes."):
        try:
            # Run the Crew process
            result = crew.kickoff(inputs={"topic": topic})
            article_content = ""

            # Parse and extract results
            if result:
                # Extracting relevant fields from JSON
                article_content = clean_header(result.raw)

                # Save the article content to session state
                st.session_state["article_content"] = article_content
            else:
                st.session_state["article_content"] = "No content generated. Please check the input."

            # Display the article content
            st.subheader("Generated Article:")
            st.text_area("Article Content", st.session_state["article_content"], height=300)

        except Exception as e:
            st.error(f"An error occurred while generating the report: {e}")
            

def create_pdf_with_wrapping(content, topic):
    # PDF setup
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Add Title
    title = f"Topic: {topic}"
    story.append(Paragraph(title, styles["Title"]))
    story.append(Spacer(1, 12))  # Spacer for better layout

    # Add Content
    paragraphs = content.split("\n")  # Split content into paragraphs
    for para in paragraphs:
        if para.strip():  # Skip empty lines
            story.append(Paragraph(para, styles["BodyText"]))
            story.append(Spacer(1, 12))  # Add spacing between paragraphs

    # Build the PDF
    doc.build(story)
    buffer.seek(0)
    return buffer


# Button to download the article as a PDF
if "article_content" in st.session_state and st.session_state["article_content"]:

    # Generate the PDF when requested
    pdf_buffer = create_pdf_with_wrapping(st.session_state["article_content"], topic)

    # Download button for the PDF file
    st.download_button(
        label="Download Report as PDF",
        data=pdf_buffer,
        file_name=f"{topic.replace(' ', '_')}_article.pdf",
        mime="application/pdf",
    )

