# Post-Migration Checklist

Use this checklist to complete your migration to a distributable Python library.

## ✅ Completed (Done by migration)

- [x] Create src layout structure
- [x] Add pyproject.toml with modern configuration
- [x] Set up hatchling build system
- [x] Add comprehensive README.md
- [x] Add LICENSE (MIT)
- [x] Add .gitignore
- [x] Add type hints marker (py.typed)
- [x] Configure pytest in pyproject.toml
- [x] Configure coverage in pyproject.toml
- [x] Configure ruff (linter/formatter)
- [x] Configure mypy (type checker)
- [x] Add CHANGELOG.md
- [x] Add CONTRIBUTING.md
- [x] Add GitHub Actions CI/CD
- [x] Build distribution packages
- [x] Add context manager support
- [x] Add version info to **init**.py
- [x] Create comprehensive documentation

## 📝 TODO: Customize for Your Project

### 1. Update Project Metadata

Edit `pyproject.toml`:

```toml
[project]
name = "pritunl-client"  # ✅ Good
authors = [
    {name = "Your Name", email = "your.email@example.com"},  # ⚠️ UPDATE THIS
]

[project.urls]
Homepage = "https://github.com/yourusername/pritunl-client"  # ⚠️ UPDATE THIS
Repository = "https://github.com/yourusername/pritunl-client"  # ⚠️ UPDATE THIS
Issues = "https://github.com/yourusername/pritunl-client/issues"  # ⚠️ UPDATE THIS
```

**Checklist:**

- [ ] Update author name
- [ ] Update author email
- [ ] Update repository URLs
- [ ] Verify project description
- [ ] Verify keywords

### 2. Update README Badges

Edit `README.md` and update these placeholders:

```markdown
[![Tests](https://github.com/yourusername/pritunl-client/workflows/tests/badge.svg)]
^^^^^^^^^^^^^ UPDATE THIS

[![Coverage](https://codecov.io/gh/yourusername/pritunl-client/branch/main/graph/badge.svg)]
^^^^^^^^^^^^^ UPDATE THIS
```

**Checklist:**

- [ ] Replace `yourusername` with actual GitHub username
- [ ] Update all badge URLs
- [ ] Test that badges work (after pushing to GitHub)

### 3. Set Up Git Repository

```bash
cd /Users/zhu/Dev/zto/vpnbot

# Initialize git (if not already)
git init

# Add all files
git add .

# Make initial commit
git commit -m "feat: modern Python package structure

- Migrate to src layout
- Add comprehensive documentation
- Configure modern tooling (uv, ruff, mypy)
- Add CI/CD with GitHub Actions
- Build distributable packages
"

# Create main branch
git branch -M main

# Add remote (create repo on GitHub first)
git remote add origin https://github.com/yourusername/pritunl-client.git

# Push
git push -u origin main
```

**Checklist:**

- [ ] Create GitHub repository
- [ ] Initialize git
- [ ] Make initial commit
- [ ] Push to GitHub
- [ ] Verify GitHub Actions runs successfully

### 4. Configure GitHub Repository

On GitHub repository settings:

**Checklist:**

- [ ] Add repository description
- [ ] Add repository topics/tags: `python`, `pritunl`, `vpn`, `api-client`
- [ ] Enable "Issues"
- [ ] Enable "Discussions" (optional)
- [ ] Configure branch protection for `main`:
  - [ ] Require status checks to pass
  - [ ] Require code review
- [ ] Add repository secrets:
  - [ ] `CODECOV_TOKEN` (from codecov.io)
  - [ ] `PYPI_API_TOKEN` (for publishing)

### 5. Set Up Coverage Reporting (Optional)

1. **Sign up at codecov.io:**

   - Go to https://codecov.io
   - Sign in with GitHub
   - Add your repository

2. **Get upload token:**

   - Go to repository settings
   - Copy upload token

3. **Add to GitHub secrets:**
   - Go to repo → Settings → Secrets → Actions
   - Add `CODECOV_TOKEN`

**Checklist:**

- [ ] Sign up for Codecov
- [ ] Add repository to Codecov
- [ ] Get upload token
- [ ] Add token to GitHub secrets
- [ ] Verify coverage uploads after CI run

### 6. Register on PyPI (For Publishing)

1. **Create PyPI account:**

   - Go to https://pypi.org
   - Create account
   - Verify email

2. **Create API token:**

   - Account settings → API tokens
   - Create token with scope for this project
   - Copy token (shown only once!)

3. **Configure uv (or add to GitHub secrets):**

   ```bash
   # Option 1: Local (for manual publishing)
   # Store in ~/.pypirc or use uv publish --token <token>

   # Option 2: GitHub Actions (for automated publishing)
   # Add PYPI_API_TOKEN to repository secrets
   ```

**Checklist:**

- [ ] Create PyPI account
- [ ] Verify email
- [ ] Create API token
- [ ] Store token securely
- [ ] (Optional) Add to GitHub secrets for auto-publish

### 7. Clean Up Old Files

Remove files that are no longer needed:

```bash
# Old package location (code now in src/)
rm -rf pritunl_client/

# Old build artifacts
rm -rf pritunl_client.egg-info/

# Old config (now in pyproject.toml)
rm requirements.txt
rm pytest.ini

# (Optional) Project notes
rm pritunl-requests.md
```

**Checklist:**

- [ ] Remove old `pritunl_client/` directory
- [ ] Remove `pritunl_client.egg-info/`
- [ ] Remove `requirements.txt`
- [ ] Remove `pytest.ini`
- [ ] (Optional) Remove `pritunl-requests.md`
- [ ] Verify tests still pass after cleanup

### 8. Test the Package Locally

```bash
# Build
uv build

# Install in a fresh environment
cd /tmp
python -m venv test-env
source test-env/bin/activate

# Install from wheel
pip install /path/to/your/dist/pritunl_client-0.1.0-py3-none-any.whl

# Test import
python -c "from pritunl_client import PritunlClient; print('Success!')"

# Test version
python -c "import pritunl_client; print(pritunl_client.__version__)"

# Clean up
deactivate
rm -rf test-env
```

**Checklist:**

- [ ] Build packages successfully
- [ ] Install from wheel works
- [ ] Import works
- [ ] Version info works
- [ ] Basic functionality works

### 9. Create First Release

```bash
# Tag the release
git tag -a v0.1.0 -m "Release v0.1.0

Initial release with:
- Full Pritunl API support
- Modern packaging structure
- Comprehensive test suite
- 100% code coverage
"

# Push tag
git push origin v0.1.0

# Build and publish
uv build
uv publish  # Or: uv publish --token <your-pypi-token>
```

**Checklist:**

- [ ] Create git tag
- [ ] Push tag to GitHub
- [ ] Build distribution
- [ ] Publish to PyPI
- [ ] Verify package on PyPI
- [ ] Test install from PyPI: `pip install pritunl-client`

### 10. Documentation

**Checklist:**

- [ ] Review README.md for accuracy
- [ ] Add usage examples
- [ ] Document all public APIs
- [ ] Add troubleshooting section (if needed)
- [ ] Create GitHub wiki (optional)
- [ ] Set up Read the Docs (optional)

### 11. Community

**Checklist:**

- [ ] Add CODE_OF_CONDUCT.md (optional)
- [ ] Add SECURITY.md with security policy (optional)
- [ ] Create issue templates (optional)
- [ ] Create PR template (optional)
- [ ] Add funding.yml for sponsors (optional)

## 🎯 Quick Verification

Run these commands to verify everything works:

```bash
# In your project directory
cd /Users/zhu/Dev/zto/vpnbot

# Activate venv
source .venv/bin/activate

# Run all checks
pytest                          # ✓ All tests pass
ruff check src tests           # ✓ No linting errors
ruff format --check src tests  # ✓ Code is formatted
mypy src                       # ✓ Type checks pass (or acceptable errors)
uv build                       # ✓ Builds successfully

# Verify package info
python -c "import pritunl_client; print(pritunl_client.__version__)"  # ✓ Shows 0.1.0
```

**All checks:**

- [ ] Tests pass (36/36)
- [ ] No linting errors
- [ ] Code properly formatted
- [ ] Type checks pass
- [ ] Builds successfully
- [ ] Version info correct

## 📊 Final Status

When everything above is complete, your project will be:

✅ **Production Ready**

- Modern package structure
- Comprehensive testing
- Type safety
- Documentation
- CI/CD pipeline

✅ **Distribution Ready**

- PyPI publishable
- Installable via pip/uv
- Proper versioning
- License included

✅ **Community Ready**

- Contributing guidelines
- Code of conduct (optional)
- Issue templates (optional)
- Clear documentation

## 🚀 Next Steps After Migration

1. **Start using it:**

   ```bash
   pip install pritunl-client
   ```

2. **Keep it updated:**

   - Bump version for releases
   - Update CHANGELOG
   - Keep dependencies updated

3. **Grow the project:**
   - Add more features
   - Improve documentation
   - Engage with users

---

**Note:** This checklist covers everything needed to complete your migration to a modern Python package. Check off items as you complete them!
