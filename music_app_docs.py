import os

# Configurable variables
app_name = "Music App"
base_folder = "music_app_docs"

# Music App specific documentation structure
files_and_prompts = {
    f"{base_folder}/00_Product/PRD.md": 
        """Create a Product Requirements Document (PRD) for a Music App that covers:
        - Vision: Create an intuitive music streaming platform
        - Target Users: Music lovers, playlist creators, artists
        - Core Features:
          * Music streaming and offline playback
          * Personalized playlists and recommendations
          * Social sharing and playlist collaboration
          * Artist profiles and music discovery
          * Lyrics integration and synchronized display
        - Success Metrics: User engagement, retention, music plays""",
    
    f"{base_folder}/01_Architecture/System_Design.md":
        """Design a system architecture for the Music App including:
        - Components:
          * Music streaming service
          * Real-time lyrics sync system
          * Recommendation engine
          * Social features backend
          * Content delivery network
        - Data flow for music streaming
        - Caching strategy for offline playback
        - Real-time sync architecture""",
    
    f"{base_folder}/01_Architecture/Tech_Stack.md":
        """Document the Music App technology choices including:
        - Frontend: 
          * Swift UI for iOS
          * Native audio frameworks
          * Core Animation for visualizations
        - Backend:
          * Audio processing services
          * Real-time streaming servers
          * Content delivery networks
        - Database:
          * User preferences and playlists
          * Music metadata and caching""",
    
    f"{base_folder}/02_Frontend/Guidelines.md":
        """Define frontend guidelines for the Music App covering:
        - UI Components:
          * Music player controls
          * Playlist management
          * Artist profiles
          * Album artwork display
        - Animations and Transitions
        - Audio Visualization
        - Offline Mode UI
        - Performance Optimization""",
    
    f"{base_folder}/02_Frontend/File_Structure.md":
        """Document the iOS app organization including:
        - Core Features:
          * Player
          * Library
          * Search
          * Radio
          * Social
        - Shared Components
        - Asset Management
        - Localization Structure""",
    
    f"{base_folder}/03_Backend/Structure.md":
        """Detail the Music App backend including:
        - API Endpoints:
          * Music streaming
          * User authentication
          * Playlist management
          * Social features
        - Real-time Services:
          * Live lyrics sync
          * Social activity
          * Play status""",
    
    f"{base_folder}/04_Flows/User_Flows.md":
        """Document key Music App user journeys:
        - Music Playback:
          * Song selection
          * Queue management
          * Playlist creation
        - Social Features:
          * Sharing songs
          * Collaborative playlists
          * Following artists
        - Offline Mode:
          * Download management
          * Offline playback""",
    
    f"{base_folder}/04_Flows/Data_Flows.md":
        """Describe Music App data workflows:
        - Music Streaming:
          * Audio buffering
          * Quality adaptation
          * Offline storage
        - Recommendation System:
          * User preference learning
          * Similar song matching
          * Playlist suggestions""",
    
    f"{base_folder}/05_AI/System_Prompts.md":
        """Document AI features for Music App:
        - Music Recommendations:
          * Personalized playlists
          * Genre classification
          * Mood-based suggestions
        - Content Generation:
          * Playlist descriptions
          * Music summaries
          * Artist bios
        - Natural Language Processing:
          * Voice search
          * Lyrics analysis
          * Music mood detection""",
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
        file.write("AI-friendly documentation structure for your Music App project.\n\n")

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