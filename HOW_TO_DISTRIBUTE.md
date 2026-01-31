# 💝 How to Distribute Your Valentine's Package

## Option 1: Test Locally First (Recommended)

Test the package on your own machine before sending:

```bash
# Install the package locally
cd /Users/leonardholter/valentines
pip3 install -e .

# Test it
valentines-surprise

# Uninstall when done testing
pip3 uninstall valentines-surprise
```

## Option 2: Share the Package Files Directly

The simplest way - just send your valentine the folder!

```bash
# Create a distribution
python3 setup.py sdist bdist_wheel

# This creates a dist/ folder with:
# - valentines-surprise-1.0.0.tar.gz
# - valentines_surprise-1.0.0-py3-none-any.whl
```

Then send them the `.tar.gz` file and tell them to run:
```bash
pip3 install valentines-surprise-1.0.0.tar.gz
```

## Option 3: Upload to PyPI (Public - Anyone Can Install)

To make it available via `pip3 install valentines-surprise`:

### Step 1: Create PyPI Account
1. Go to https://pypi.org/account/register/
2. Create an account
3. Verify your email

### Step 2: Install Upload Tools
```bash
pip3 install twine
```

### Step 3: Build the Package
```bash
cd /Users/leonardholter/valentines
python3 setup.py sdist bdist_wheel
```

### Step 4: Upload to PyPI
```bash
twine upload dist/*
```

You'll be prompted for your PyPI username and password.

**Note:** The package name must be unique on PyPI. If `valentines-surprise` is taken, you'll need to change it in `setup.py` (e.g., `valentines-surprise-2026` or `your-name-valentine`).

## Option 4: Private Distribution (TestPyPI)

Test on TestPyPI first before the real PyPI:

1. Create account at https://test.pypi.org/account/register/
2. Upload:
```bash
twine upload --repository testpypi dist/*
```
3. Install from TestPyPI:
```bash
pip3 install --index-url https://test.pypi.org/simple/ valentines-surprise
```

## 🎁 Customization

Before distributing, you can customize the message in `valentines_surprise/__init__.py` and `setup.py` to make it more personal!

Edit the text between the triple quotes to add your own sweet words. 💕

## Tips for Your Valentine

### Option A: Install and show with their name

Tell them to run these commands (replace "Emily" with their name):

```bash
pip3 install valentines-surprise
valentines-surprise "Emily"
```

This will display: **"💝 WILL YOU BE MY VALENTINE, EMILY? 💝"**

### Option B: Just install (shows generic message during installation)

> "Hey! I made something special for you. Just run this command in your terminal:
> 
> `pip3 install valentines-surprise`
> 
> 💝"

### If sharing the file directly:

> "I created a special package for you! Download the attached file and run:
> 
> ```bash
> pip3 install valentines-surprise-1.0.0.tar.gz
> valentines-surprise "Your Name"
> ```
> 
> 💝"

## Usage After Installation

Your valentine can run the surprise anytime with:

```bash
# With their name
valentines-surprise "Emily"

# Without a name (generic message)
valentines-surprise
```
