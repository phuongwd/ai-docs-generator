# Documentation Generator 📚

A Python-based documentation generator that creates a well-structured, hierarchical documentation template for your projects. This tool automatically generates a comprehensive documentation structure with consistent formatting and helpful prompts for content creation.

## Features ✨

- 🗂️ Creates a complete, two-level documentation structure
- 📝 Generates template files with consistent formatting
- 🎯 Includes AI prompts for content guidance
- 🔍 Supports metadata for better searchability
- 📚 Creates an index with emoji-enhanced navigation for both sections and subsections
- 🎨 Maintains consistent styling across all documents

## Documentation Structure 📁

The generator creates a comprehensive documentation structure:

```text
docs/
├── 00_Getting_Started/          # 🚀 Quick start and installation guides
├── 01_Project_Overview/         # 📌 Project background and context
├── 02_Feature_Definitions/      # ✨ Core and additional features
├── 03_Technical_Requirements/   # ⚙️ Architecture and technical specs
│   ├── Database_Design/        # 💾 Database architecture
│   ├── User_Flows/            # 🔄 User journey documentation
│   └── Flow_Diagrams/         # 📊 Visual flow representations
├── 04_UI_UX_Guidelines/         # 🎨 Design principles and standards
├── 05_Testing_Strategy/         # ✅ Testing approach and cases
│   └── Test_Cases/            # 🧪 Test specifications
├── 06_Deployment_and_Next_Steps/# 🚀 Deployment and roadmap
├── 07_Development_Guides/       # 💻 Development standards
├── 08_API_Documentation/        # 🔌 API specifications
├── 09_Deployment/              # 📦 Deployment configurations
├── 10_Support/                 # 💡 FAQs and troubleshooting
├── 11_Security/                # 🔒 Security guidelines
└── Assets/                     # 🎨 Project assets
    └── Style_Guides/          # 🎨 Design guidelines
```

## Generated Index Structure 📋

The generator creates an index with:
- Main sections with emojis (e.g., "## 📌 Project Overview")
- Subsections with relevant emojis (e.g., "### 💾 Database Design")
- Organized links to all documentation files
- Clear hierarchy for easy navigation

## File Organization 🗄️

The documentation is organized in a two-level hierarchy:
1. **Main Sections**: Primary categories with leading numbers (00-11)
   - Each section has its unique emoji identifier
   - Consistent formatting across all sections
2. **Subsections**: Specific topics within each category
   - Each subsection has its relevant emoji
   - Grouped under their parent section
   - Maintains clear relationship with main section

## Quick Start 🚀

1. **Installation**
   ```bash
   # Clone the repository
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Configuration**
   ```python
   # Modify the variables in generate_docs.py
   app_name = "Your App Name"
   base_folder = "docs"  # or your preferred output directory
   ```

3. **Generate Documentation**
   ```bash
   python generate_docs.py
   ```

## Generated File Structure 📋

Each generated markdown file includes:
- Frontmatter with metadata
- Last updated timestamp
- Document status
- Table of contents
- Standard sections (Overview, Details, Examples, Related)
- AI prompts for content generation

## Customization 🛠️

You can customize the documentation structure by:
1. Modifying the `files_and_prompts` dictionary
2. Adding new sections in the emoji mapping
3. Creating custom prompt patterns
4. Adjusting the file template structure

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Support 💬

If you have any questions or need help:
1. Check the generated documentation
2. Open an issue in the repository
3. Refer to the troubleshooting guide
