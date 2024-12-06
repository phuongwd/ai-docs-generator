import os

# Configurable variables
app_name = "My App"
base_folder = "ai_docs"

# Simplified structure focusing on AI-friendly documentation
files_and_prompts = {
    f"{base_folder}/00_Product/PRD.md": 
        """Create a Product Requirements Document (PRD) that covers:
        - Product vision and objectives
        - Target audience and user personas
        - Core features and functionalities
        - User stories and acceptance criteria
        - Success metrics and KPIs""",
    
    f"{base_folder}/01_Architecture/System_Design.md":
        """Design a system architecture that includes:
        - High-level system components
        - Data flow between components
        - API design principles
        - Security considerations
        - Scalability approach""",
    
    f"{base_folder}/01_Architecture/Tech_Stack.md":
        """Document the technology choices including:
        - Frontend framework and libraries
        - Backend technologies
        - Database solutions
        - DevOps tools
        - Rationale for each choice""",
    
    f"{base_folder}/02_Frontend/Guidelines.md":
        """Define frontend development standards covering:
        - Component architecture
        - State management
        - Styling approach
        - Performance optimization
        - Code organization""",
    
    f"{base_folder}/02_Frontend/File_Structure.md":
        """Document the frontend organization including:
        - Directory structure
        - File naming conventions
        - Module organization
        - Asset management
        - Build configuration""",
    
    f"{base_folder}/03_Backend/Structure.md":
        """Detail the backend architecture including:
        - API endpoints and methods
        - Database schema
        - Authentication flow
        - Error handling
        - Performance considerations""",
    
    f"{base_folder}/04_Flows/User_Flows.md":
        """Document key user journeys including:
        - Authentication flows
        - Main feature workflows
        - Error scenarios
        - Edge cases
        - Success states""",
    
    f"{base_folder}/04_Flows/Data_Flows.md":
        """Describe data workflows including:
        - Data validation
        - Processing steps
        - Storage procedures
        - Caching strategy
        - Error handling""",
    
    f"{base_folder}/05_AI/System_Prompts.md":
        """Document AI integration patterns including:
        - System prompt templates
        - Context injection methods
        - Response handling
        - Error recovery
        - Best practices for AI interactions
        - Prompt engineering guidelines
        - Model-specific optimizations
        - Token usage considerations""",
}

def create_file(path, prompt):
    """Create a markdown file with AI-friendly structure."""
    title = os.path.basename(path).replace('_', ' ').replace('.md', '')
    
    with open(path, 'w') as file:
        file.write(f"# {title}\n\n")
        
        # Add AI context section
        file.write("## 🤖 AI Context\n\n")
        file.write("_Provide context about this document to AI_\n\n")
        
        # Add main content sections
        file.write("## 📝 Content\n\n")
        file.write("_Main content goes here_\n\n")
        
        # Add the AI prompt as a guide
        file.write(f"## 💡 AI Prompt\n\n")
        file.write(f"{prompt}\n\n")
        
        # Add examples section
        file.write("## 📋 Examples\n\n")
        file.write("_Add relevant examples here_\n\n")
    
    print(f"Created: {path}")

def create_index():
    """Create an index file with links to all documentation."""
    index_path = f"{base_folder}/00_Index.md"
    
    with open(index_path, 'w') as file:
        file.write(f"# 📚 {app_name} Documentation\n\n")
        file.write("AI-friendly documentation structure for your project.\n\n")

        # Organize files by sections
        sections = {}
        for path in files_and_prompts.keys():
            if path != index_path:
                relative_path = path.replace(f"{base_folder}/", "")
                section = relative_path.split("/")[0].split("_", 1)[1]  # Remove number prefix
                if section not in sections:
                    sections[section] = []
                sections[section].append((os.path.basename(path).replace(".md", "").replace("_", " "), relative_path))

        # Emoji mapping for sections
        emoji_mapping = {
            "Product": "📋",
            "Architecture": "🏗️",
            "Frontend": "💻",
            "Backend": "⚙️",
            "Flows": "🔄",
            "AI": "🤖"
        }

        # Write sections
        for section, files in sections.items():
            emoji = emoji_mapping.get(section, "📄")
            file.write(f"## {emoji} {section}\n\n")
            for name, path in sorted(files):
                file.write(f"- [{name}]({path})\n")
            file.write("\n")

        file.write("\n---\n\n")
        file.write("Generated with AI Documentation Generator 🤖\n")
    
    print(f"Created: {index_path}")

def main():
    """Generate AI-friendly documentation structure."""
    for path, prompt in files_and_prompts.items():
        dir_name = os.path.dirname(path)
        os.makedirs(dir_name, exist_ok=True)
        if not os.path.exists(path):
            create_file(path, prompt)
    
    # Create index file
    create_index()
    print("✨ Documentation structure created successfully!")

if __name__ == "__main__":
    main() 