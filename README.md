This repository contains both the backend and frontend parts of the project, each with its own setup and dependencies.

The backend is built using Python and PyTorch, designed to handle AI/ML tasks and API services. To keep the repository clean and manageable, the Python virtual environment folder (backend/venv) is excluded from the Git history, as it contains many large files and binaries that are unnecessary to track in version control. Before running the backend, you will need to create and activate this virtual environment on your local machine and install the required Python packages listed in requirements.txt. This ensures all dependencies are correctly installed without bloating the repository.

The frontend is developed using a modern JavaScript framework (such as React or another) and requires Node.js and npm/yarn to manage dependencies. After navigating to the frontend directory, install all frontend dependencies via npm install or yarn install, and run the development server using npm start or yarn start.

Since the frontend communicates with the backend APIs, make sure the backend server is running before launching the frontend application to enable smooth interaction between the two.

Additionally, large files such as pretrained model binaries or libraries (e.g., PyTorch DLLs) are not pushed to the repository to avoid exceeding GitHub’s file size limits. You may need to manage or download these files separately as per your project requirements.

This approach keeps the repository lightweight and focused on source code, while allowing you to easily set up a complete development environment by following the setup instructions for both backend and frontend.

