import os

# Configurable variables
app_name = "My App"
base_folder = "docs_example"

def get_prompt_by_pattern(key):
    """Generate prompts based on predefined patterns"""
    
    # Base prompts for documentation sections
    base_prompts = {
        # Index and Overview
        "Index": "Provide a comprehensive overview of the documentation structure and navigation guide.",
        "Overview": "Provide a high-level overview of {topic}, including its purpose, goals, and target audience.",
        "Background_and_Context": "Explain the background, context, and market need that {topic} addresses.",
        
        # Features
        "Core_Features": "List and describe the essential features of {topic}, explaining the importance of each component.",
        "Additional_Features": "Describe potential additional features that could enhance {topic} functionality.",
        "User_Stories_and_Use_Cases": "Document key user stories and use cases, including user goals and expected outcomes.",
        
        # Technical
        "Architecture": "Detail the system architecture, including components, interactions, and technical decisions.",
        "Technology_Stack": "Document the complete technology stack, including tools, frameworks, and their purposes.",
        "API_Specifications": "Specify the API endpoints, request/response formats, and integration details.",
        "Data_Flow_Diagrams": "Create detailed data flow diagrams showing system interactions and data movement.",
        
        # UI/UX
        "UI_UX_Guidelines": "Define UI/UX principles and guidelines for maintaining consistency and usability.",
        "Design_Principles": "Outline the core design principles and their implementation in the interface.",
        "Accessibility_Standards": "Document accessibility requirements and implementation guidelines.",
        
        # Testing
        "Test_Plan": "Outline the testing strategy, including test types, coverage, and success criteria.",
        "User_Interaction": "Define test scenarios for validating user interactions and experiences.",
        "Metrics_for_Success": "Specify key performance indicators and success metrics.",
        
        # Deployment and Planning
        "Deployment_Plan": "Detail the deployment strategy, including environments, steps, and verification.",
        "Roadmap": "Outline the development roadmap, including milestones and feature releases.",
        "Risk_Analysis": "Identify potential risks and their mitigation strategies.",
        
        # Style Guides
        "Typography": "Define typography standards, including fonts, sizes, and usage guidelines.",
        "Colors": "Specify the color palette, usage rules, and accessibility considerations.",
        
        # Database Design
        "Database_Schema": "Document the database schema, including tables, relationships, and field specifications.",
        "Data_Models": "Define the data models and their relationships within the application.",
        "Database_Migration": "Outline the database migration strategy and version control approach.",
        "Query_Optimization": "Document database query optimization strategies and indexing approach.",
    }
    
    # Flow-specific prompts
    flow_prompts = {
        "Main_User_Journey": "Document the end-to-end user journey, including key touchpoints and decisions.",
        "Registration_Flow": "Detail the complete registration process flow and requirements.",
        "Settings_Management_Flow": "Describe the settings management workflow and configuration options.",
        "Error_Recovery_Flow": "Document error scenarios and recovery procedures.",
        "Feedback_Loop_Flow": "Explain the feedback collection and processing workflow.",
        "Practice_Flow": "Detail the main interaction flow from start to completion.",
        "Progress_Tracking_Flow": "Document the progress monitoring and reporting workflow.",
    }
    
    # First check if it's a flow
    if key.endswith('_Flow'):
        return flow_prompts.get(key, f"Document the complete flow for {key.replace('_Flow', '')}")
    
    # Then check base prompts
    return base_prompts.get(key, f"Document the specifications for {key.replace('_', ' ').lower()}")

# Define files and their respective prompts
files_and_prompts = {
    f"{base_folder}/00_Index.md": 
        get_prompt_by_pattern("Index"),
    f"{base_folder}/01_Project_Overview/Overview.md": 
        get_prompt_by_pattern("Project_Overview"),
    f"{base_folder}/01_Project_Overview/Background_and_Context.md": 
        get_prompt_by_pattern("Background_and_Context"),
    f"{base_folder}/02_Feature_Definitions/Core_Features.md": 
        get_prompt_by_pattern("Core_Features"),
    f"{base_folder}/02_Feature_Definitions/Additional_Features.md": 
        get_prompt_by_pattern("Additional_Features"),
    f"{base_folder}/02_Feature_Definitions/User_Stories_and_Use_Cases.md": 
        get_prompt_by_pattern("User_Stories_and_Use_Cases"),
    f"{base_folder}/03_Technical_Requirements/System_Architecture.md": 
        get_prompt_by_pattern("Architecture"),
    f"{base_folder}/03_Technical_Requirements/Technology_Stack.md": 
        get_prompt_by_pattern("Technology_Stack"),
    f"{base_folder}/03_Technical_Requirements/API_Specifications.md": 
        get_prompt_by_pattern("API_Specifications"),
    f"{base_folder}/03_Technical_Requirements/Data_Flow_Diagrams.md": 
        get_prompt_by_pattern("Data_Flow_Diagrams"),
    f"{base_folder}/04_UI_UX_Guidelines/Design_Principles.md": 
        get_prompt_by_pattern("UI_UX_Guidelines"),
    f"{base_folder}/04_UI_UX_Guidelines/Wireframes/Home_Screen.png": 
        "Create wireframe ideas for the application home screen.",
    f"{base_folder}/04_UI_UX_Guidelines/Wireframes/Practice_Mode.png": 
        "Generate wireframe ideas for the main interaction screens.",
    f"{base_folder}/04_UI_UX_Guidelines/Accessibility_Standards.md": 
        "What accessibility standards should be applied for an application designed for global users?",
    f"{base_folder}/05_Testing_Strategy/Test_Plan.md": 
        get_prompt_by_pattern("Test_Plan"),
    f"{base_folder}/05_Testing_Strategy/Test_Cases/Core_Features.md": 
        get_prompt_by_pattern("Core_Features"),
    f"{base_folder}/05_Testing_Strategy/Test_Cases/User_Interaction.md": 
        get_prompt_by_pattern("User_Interaction"),
    f"{base_folder}/05_Testing_Strategy/Metrics_for_Success.md": 
        get_prompt_by_pattern("Metrics_for_Success"),
    f"{base_folder}/06_Deployment_and_Next_Steps/Deployment_Plan.md": 
        get_prompt_by_pattern("Deployment_Plan"),
    f"{base_folder}/06_Deployment_and_Next_Steps/Roadmap.md": 
        get_prompt_by_pattern("Roadmap"),
    f"{base_folder}/06_Deployment_and_Next_Steps/Risk_Analysis.md": 
        get_prompt_by_pattern("Risk_Analysis"),
    f"{base_folder}/Assets/Style_Guides/Typography.md": 
        get_prompt_by_pattern("Typography"),
    f"{base_folder}/Assets/Style_Guides/Colors.md": 
        get_prompt_by_pattern("Colors"),
    f"{base_folder}/03_Technical_Requirements/User_Flows/Main_User_Journey.md":
        get_prompt_by_pattern("Main_User_Journey"),
    
    f"{base_folder}/03_Technical_Requirements/User_Flows/Registration_Flow.md":
        get_prompt_by_pattern("Registration_Flow"),
    
    f"{base_folder}/03_Technical_Requirements/User_Flows/Practice_Session_Flow.md":
        get_prompt_by_pattern("Practice_Session_Flow"),
    
    f"{base_folder}/03_Technical_Requirements/User_Flows/Progress_Tracking_Flow.md":
        get_prompt_by_pattern("Progress_Tracking_Flow"),
    
    f"{base_folder}/03_Technical_Requirements/User_Flows/Settings_Management_Flow.md":
        get_prompt_by_pattern("Settings_Management_Flow"),
    
    f"{base_folder}/03_Technical_Requirements/User_Flows/Error_Recovery_Flow.md":
        get_prompt_by_pattern("Error_Recovery_Flow"),
    
    f"{base_folder}/03_Technical_Requirements/User_Flows/Feedback_Loop_Flow.md":
        get_prompt_by_pattern("Feedback_Loop_Flow"),

    # Flow Diagrams
    f"{base_folder}/03_Technical_Requirements/Flow_Diagrams/Registration_Flow.md":
        get_prompt_by_pattern("Registration_Flow"),
    
    f"{base_folder}/03_Technical_Requirements/Flow_Diagrams/Practice_Flow.md":
        get_prompt_by_pattern("Practice_Flow"),
    
    f"{base_folder}/03_Technical_Requirements/Flow_Diagrams/Progress_Tracking_Flow.md":
        get_prompt_by_pattern("Progress_Tracking_Flow"),

    # Getting Started Section
    f"{base_folder}/00_Getting_Started/Quick_Start.md":
        "Step-by-step guide to get started with the app, including installation and basic usage.",
    f"{base_folder}/00_Getting_Started/Installation.md":
        "Detailed installation instructions for developers, including environment setup and dependencies.",
    f"{base_folder}/00_Getting_Started/Contributing.md":
        "Guidelines for contributing to the project, including code standards and PR process.",
    
    # Development Guides
    f"{base_folder}/07_Development_Guides/Code_Style.md":
        "Coding standards and style guidelines for maintaining consistent code quality.",
    f"{base_folder}/07_Development_Guides/State_Management.md":
        "Patterns and best practices for state management in the app.",
    f"{base_folder}/07_Development_Guides/Error_Handling.md":
        "Strategies and patterns for handling errors and exceptions.",
    f"{base_folder}/07_Development_Guides/Testing_Guide.md":
        "Comprehensive guide to testing, including unit, integration, and E2E tests.",
    
    # API Documentation
    f"{base_folder}/08_API_Documentation/API_Overview.md":
        "Overview of the API architecture and general principles.",
    f"{base_folder}/08_API_Documentation/Authentication.md":
        "Authentication methods and security implementations.",
    f"{base_folder}/08_API_Documentation/Endpoints.md":
        "Detailed documentation of all API endpoints and their usage.",
    
    # Deployment
    f"{base_folder}/09_Deployment/Vercel_Setup.md":
        "Guide to deploying the documentation on Vercel, including configuration.",
    f"{base_folder}/09_Deployment/Environment_Variables.md":
        "Documentation of all environment variables and their configuration.",
    
    # FAQ and Troubleshooting
    f"{base_folder}/10_Support/FAQ.md":
        "Frequently asked questions and their answers.",
    f"{base_folder}/10_Support/Troubleshooting.md":
        "Common issues and their solutions.",
    
    # Security
    f"{base_folder}/11_Security/Security_Best_Practices.md":
        "Security guidelines and best practices for the app.",
    f"{base_folder}/11_Security/Data_Privacy.md":
        "Data privacy considerations and implementations.",
    
    # Database Design Section
    f"{base_folder}/03_Technical_Requirements/Database_Design/Schema.md":
        get_prompt_by_pattern("Database_Schema"),
    
    f"{base_folder}/03_Technical_Requirements/Database_Design/Models.md":
        get_prompt_by_pattern("Data_Models"),
    
    f"{base_folder}/03_Technical_Requirements/Database_Design/Migrations.md":
        get_prompt_by_pattern("Database_Migration"),
    
    f"{base_folder}/03_Technical_Requirements/Database_Design/Query_Optimization.md":
        get_prompt_by_pattern("Query_Optimization"),
    
    f"{base_folder}/03_Technical_Requirements/Database_Design/ERD.md":
        "Create Entity Relationship Diagrams showing the database structure and relationships.",
}

def create_file(path, prompt):
    """Create a markdown file with a title and a suggested AI prompt."""
    title = os.path.basename(path).replace('_', ' ').replace('.md', '')
    
    with open(path, 'w') as file:
        # Add search metadata
        file.write("---\n")
        file.write(f"title: {title}\n")
        file.write("description: " + prompt.split('.')[0] + "\n")
        file.write("search:\n")
        file.write("  exclude: false\n")
        file.write("  boost: 2\n")
        file.write("---\n\n")
        
        # Add metadata section
        file.write("## Metadata\n\n")
        file.write("- **Last Updated**: YYYY-MM-DD\n")
        file.write("- **Type**: Documentation\n")
        file.write("- **Status**: Draft\n\n")
        
        # Add table of contents placeholder
        file.write("## Table of Contents\n\n")
        file.write("- [Overview](#overview)\n")
        file.write("- [Details](#details)\n")
        file.write("- [Examples](#examples)\n")
        file.write("- [Related](#related)\n\n")
        
        # Add content sections
        file.write("## Overview\n\n")
        file.write("_Add a brief overview here_\n\n")
        
        file.write("## Details\n\n")
        file.write("_Add detailed information here_\n\n")
        
        file.write("## Examples\n\n")
        file.write("```typescript\n// Add code examples here\n```\n\n")
        
        file.write("## Related\n\n")
        file.write("- [Link to related documentation]()\n\n")
        
        # Add the AI prompt as a comment
        file.write(f"<!--\n### Suggested AI Prompt:\n{prompt}\n-->\n")
    
    print(f"Created file: {path}")

def create_directory_structure():
    """Create directories and files based on the defined structure."""
    for path, prompt in files_and_prompts.items():
        dir_name = os.path.dirname(path)
        os.makedirs(dir_name, exist_ok=True)
        if not os.path.exists(path) and path.endswith('.md'):
            create_file(path, prompt)

def format_section_name(folder_name):
    """Format the section name to match emoji mapping keys."""
    # Remove leading numbers and underscores (e.g., "01_Project_Overview" -> "Project Overview")
    clean_name = ' '.join(folder_name.split('_')[1:]) if '_' in folder_name else folder_name
    
    # Special case for "UI UX Guidelines"
    if "ui ux" in clean_name.lower():
        return "UI/UX Guidelines"
    
    return clean_name.title()

def create_index_file():
    """Create an enhanced index file with emojis and two-level hierarchy."""
    index_path = f"{base_folder}/00_Index.md"
    with open(index_path, 'w') as index_file:
        index_file.write(f"# 📚 {app_name} Documentation Index\n\n")
        index_file.write(f"Welcome to the **documentation** for the {app_name}. Below is an organized list of all sections, categorized for easy navigation.\n\n")

        emoji_mapping = {
            "Getting Started": "🚀",
            "Project Overview": "📌",
            "Feature Definitions": "✨",
            "Technical Requirements": "⚙️",
            "UI UX Guidelines": "🎨",
            "Testing Strategy": "✅",
            "Development Guides": "💻",
            "API Documentation": "🔌",
            "Deployment": "📦",
            "Support": "💡",
            "Security": "🔒",
            "Deployment and Next Steps": "🚀",
            "Assets": "🎨",

            # Subsections
            "Database Design": "💾",
            "User Flows": "🔄",
            "Flow Diagrams": "📊",
            "Test Cases": "🧪",
            "Style Guides": "🎨"
        }

        # Group files by their main sections and subsections
        sections = {}
        for path in files_and_prompts.keys():
            if path != index_path and path.endswith(".md"):
                relative_path = path.replace(f"{base_folder}/", "")
                path_parts = relative_path.split("/")
                
                # Keep original section name for sorting
                main_section_original = path_parts[0]
                
                # Get display name (remove numbers and underscores)
                main_section_display = main_section_original
                if "_" in main_section_original:
                    # Handle both cases: "01_Project_Overview" and "10_Support"
                    parts = main_section_original.split("_")
                    if parts[0].isdigit():  # Remove leading number if it exists
                        parts = parts[1:]
                    main_section_display = " ".join(parts)
                    
                    # Special case handling
                    if main_section_display.lower() == "ui ux guidelines":
                        main_section_display = "UI UX Guidelines"
                    elif main_section_display.lower() == "deployment and next steps":
                        main_section_display = "Deployment and Next Steps"
                
                # Get subsection if it exists
                subsection = path_parts[1] if len(path_parts) > 2 else None
                if subsection and "_" in subsection:
                    subsection = subsection.replace("_", " ")
                
                # Get file name
                file_name = os.path.basename(path).replace("_", " ").replace(".md", "")
                
                # Organize into nested structure using original name as key
                if main_section_original not in sections:
                    sections[main_section_original] = {
                        "display_name": main_section_display,
                        "subsections": {},
                        "main": []
                    }
                
                if subsection:
                    if subsection not in sections[main_section_original]["subsections"]:
                        sections[main_section_original]["subsections"][subsection] = []
                    sections[main_section_original]["subsections"][subsection].append((file_name, relative_path))
                else:
                    sections[main_section_original]["main"].append((file_name, relative_path))

        # Write sections in order (they'll be naturally sorted by the numbered prefixes)
        for section_original in sorted(sections.keys()):
            section_info = sections[section_original]
            section_display = section_info["display_name"]
            emoji = emoji_mapping.get(section_display, "")
            
            index_file.write(f"## {emoji} {section_display}\n")
            
            # Write main files first
            for name, link in section_info["main"]:
                index_file.write(f"- [{name}]({link})\n")
            
            # Write subsections with emojis
            for subsection, items in sorted(section_info["subsections"].items()):
                if items:  # Only write subsection if it has items
                    # Get emoji for subsection
                    subsection_emoji = emoji_mapping.get(subsection, "")
                    index_file.write(f"\n### {subsection_emoji} {subsection}\n")
                    for name, link in items:
                        index_file.write(f"- [{name}]({link})\n")
            
            index_file.write("\n")

        index_file.write("Thank you for exploring this documentation. For questions, please refer to the individual files for specific guidance.\n")
    print(f"Created index file: {index_path}")

def create_documentation(app_name, base_folder, sections=None):
    """Create documentation with specified configuration"""
    # Implementation that uses the existing code but makes it more configurable

def main():
    """Main function to create the documentation structure."""
    create_directory_structure()
    create_index_file()
    print("Folder structure with emoji-enhanced index file created successfully!")

if __name__ == "__main__":
    main()
