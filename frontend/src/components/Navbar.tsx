const Navbar: React.FC = () => {
  return (
    <nav className="navbar navbar-expand-lg glass-navbar">
      <div className="container-fluid justify-content-center">
        {/* Toggle button for mobile */}
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarIcons"
          aria-controls="navbarIcons"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon" />
        </button>

        {/* Icon links */}
        <div
          className="collapse navbar-collapse justify-content-center"
          id="navbarIcons"
        >
          <ul className="navbar-nav d-flex flex-row gap-4">
            <li className="nav-item">
              <a
                className="nav-link"
                href="/nouveau-document"
                title="Nouveau document"
              >
                <i className="bi bi-file-earmark-plus large-icon"></i>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/historique" title="Historique">
                <i className="bi bi-archive large-icon"></i>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/clients" title="Clients">
                <i className="bi bi-people large-icon"></i>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/profile" title="Profil">
                <i className="bi bi-building large-icon"></i>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
