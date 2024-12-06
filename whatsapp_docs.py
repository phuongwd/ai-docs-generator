import os

# Configurable variables
app_name = "WhatsApp"
base_folder = "whatsapp_docs"

# WhatsApp specific documentation structure
files_and_prompts = {
    f"{base_folder}/00_Product/PRD.md": 
        """Create a Product Requirements Document (PRD) for WhatsApp that covers:
        - Vision: Build a secure, reliable messaging platform for everyone
        - Target Users: Global users, families, groups, businesses
        - Core Features:
          * End-to-end encrypted messaging
          * Voice and video calls
          * Media sharing and storage
          * Group conversations
          * Status updates
          * Business messaging
        - Success Metrics: Daily active users, message volume, call minutes""",
    
    f"{base_folder}/01_Architecture/System_Design.md":
        """Design a system architecture for WhatsApp including:
        - Components:
          * Message delivery system
          * End-to-end encryption
          * Media processing pipeline
          * Call infrastructure
          * Contact sync system
        - Scalability approach
        - Security architecture
        - Global distribution strategy""",
    
    f"{base_folder}/01_Architecture/Tech_Stack.md":
        """Document the WhatsApp technology choices including:
        - Mobile Apps:
          * Native iOS (Swift/Objective-C)
          * Native Android (Kotlin/Java)
        - Backend:
          * Message routing servers
          * Media processing services
          * TURN/STUN servers for calls
        - Storage:
          * Message queues
          * Media storage
          * User metadata""",
    
    f"{base_folder}/02_Frontend/Guidelines.md":
        """Define frontend guidelines for WhatsApp covering:
        - UI Components:
          * Chat interface
          * Media viewer
          * Call screens
          * Status viewer
          * Settings
        - Animations
        - Offline support
        - Media handling""",
    
    f"{base_folder}/02_Frontend/File_Structure.md":
        """Document the mobile app organization including:
        - Core Modules:
          * Messaging
          * Calls
          * Media
          * Contacts
          * Settings
        - Shared Components
        - Local Storage
        - Encryption Layer""",
    
    f"{base_folder}/03_Backend/Structure.md":
        """Detail the WhatsApp backend including:
        - Services:
          * Message routing
          * Media processing
          * Call signaling
          * Contact sync
          * Status delivery
        - Security:
          * E2E encryption
          * Key management
          * Privacy controls""",
    
    f"{base_folder}/04_Flows/User_Flows.md":
        """Document key WhatsApp user journeys:
        - Messaging:
          * One-to-one chats
          * Group conversations
          * Broadcast lists
          * Message reactions
        - Media Sharing:
          * Photo/video sharing
          * Document sharing
          * Location sharing
        - Calls:
          * Voice calls
          * Video calls
          * Group calls""",
    
    f"{base_folder}/04_Flows/Data_Flows.md":
        """Describe WhatsApp data workflows:
        - Message Flow:
          * Encryption process
          * Delivery system
          * Receipt confirmation
        - Media Processing:
          * Upload pipeline
          * Compression
          * Storage optimization
        - Call Setup:
          * Signaling
          * Peer connection
          * Quality optimization""",
    
    f"{base_folder}/05_AI/System_Prompts.md":
        """Document AI features for WhatsApp:
        - Message Features:
          * Smart replies
          * Text prediction
          * Language detection
        - Media Intelligence:
          * Image recognition
          * Sticker suggestions
          * Voice recognition
        - Security:
          * Spam detection
          * Abuse prevention
          * Content moderation
        - Business Features:
          * Automated responses
          * Customer segmentation
          * Engagement analytics""",
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
        file.write("AI-friendly documentation structure for your WhatsApp project.\n\n")

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