# study.python-basics

## StudyFlow 📒

#### 1. Create Environment

```
 python -m venv myEnv   (Windows)  🐍
 python3 -m venv myEnv  (Linux)    🐧
```

#### 2. Activate the Environment

- ## 📂 Windows:

```powershell
  cd C:\Users\user\Documents\github
  cd C:\Users\user\Documents\python.Env
  python -m venv myEnv
```

  **Script Disabled for this system**

```powershell
 Set-ExecutionPolicy RemoteSigned –Scope Process
 cd C:\Users\user\Documents\python.Env\myEnv\Scripts\
 Activate.ps1
```

## 🐧 Linux:

```bash
  source ~/Desktop/docs/myPython/myEnv/bin/activate
  source ~/Path/to/myEnv/bin/activate
```

#### 3. Install Packages

```
- 📦 pip install <Package name>
- 📦 pip install -r requirements.txt
- 📋 pip list
```

**Finally, when you're done:** `deactivate`
