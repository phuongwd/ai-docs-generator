import os

# Configurable variables
app_name = "Slack App"
base_folder = "slack_app_docs"

# Slack App specific documentation structure
files_and_prompts = {
    f"{base_folder}/00_Product/PRD.md": 
        """Create a Product Requirements Document (PRD) for a Slack App that covers:
        - Vision: Create a powerful workplace communication platform
        - Target Users: Teams, organizations, remote workers
        - Core Features:
          * Real-time messaging and threads
          * Channel management and organization
          * File sharing and collaboration
          * App integrations and workflows
          * Search and message history
        - Success Metrics: Daily active users, message engagement, workspace adoption""",
    
    f"{base_folder}/01_Architecture/System_Design.md":
        """Design a system architecture for the Slack App including:
        - Components:
          * Real-time messaging service
          * WebSocket connections
          * Message persistence layer
          * Search indexing service
          * File storage system
        - Data flow for instant messaging
        - Caching strategy for message history
        - Real-time event architecture""",
    
    f"{base_folder}/01_Architecture/Tech_Stack.md":
        """Document the Slack App technology choices including:
        - Frontend: 
          * React for web client
          * Electron for desktop app
          * React Native for mobile
        - Backend:
          * WebSocket servers
          * Message queuing system
          * Search infrastructure
        - Database:
          * Message storage
          * User and workspace data
          * File metadata""",
    
    f"{base_folder}/02_Frontend/Guidelines.md":
        """Define frontend guidelines for the Slack App covering:
        - UI Components:
          * Message composer
          * Channel sidebar
          * Thread views
          * Search interface
        - Real-time Updates
        - Message Formatting
        - File Preview
        - Performance Optimization""",
    
    f"{base_folder}/02_Frontend/File_Structure.md":
        """Document the app organization including:
        - Core Features:
          * Messaging
          * Channels
          * Search
          * Files
          * Apps
        - Shared Components
        - State Management
        - Real-time Updates""",
    
    f"{base_folder}/03_Backend/Structure.md":
        """Detail the Slack App backend including:
        - API Endpoints:
          * Message operations
          * Channel management
          * User authentication
          * File handling
        - Real-time Services:
          * WebSocket connections
          * Presence system
          * Typing indicators
          * Message delivery""",
    
    f"{base_folder}/04_Flows/User_Flows.md":
        """Document key Slack App user journeys:
        - Messaging:
          * Direct messages
          * Channel messages
          * Thread interactions
          * File sharing
        - Workspace:
          * Channel creation
          * User invitations
          * App installations
        - Search:
          * Message search
          * File search
          * Advanced filters""",
    
    f"{base_folder}/04_Flows/Data_Flows.md":
        """Describe Slack App data workflows:
        - Message Handling:
          * Message composition
          * Real-time delivery
          * Storage and indexing
        - File Management:
          * Upload process
          * Preview generation
          * Storage optimization
        - Search System:
          * Indexing pipeline
          * Query processing
          * Result ranking""",
    
    f"{base_folder}/05_AI/System_Prompts.md":
        """Document AI features for Slack App:
        - Message Enhancement:
          * Smart replies
          * Message summarization
          * Content recommendations
        - Search Intelligence:
          * Natural language search
          * Semantic matching
          * Relevance ranking
        - Workflow Automation:
          * Task detection
          * Meeting scheduling
          * Information extraction
        - User Experience:
          * Channel recommendations
          * Priority messaging
          * Focus time suggestions""",
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
        file.write("AI-friendly documentation structure for your Slack App project.\n\n")

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