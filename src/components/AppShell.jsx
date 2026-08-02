import React, { useState, useEffect, useCallback } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import {
  BookOpen,
  GraduationCap,
  ChevronRight,
  Menu,
  X,
  Home,
  FileText,
  Layers,
  NotebookPen,
  Brain,
  ChevronDown,
  ChevronUp,
  Sparkles,
} from 'lucide-react';

const SIDEBAR_WIDTH = 248;

// Navigation tree
const NAV_ITEMS = [
  {
    id: 'home',
    label: 'Home',
    icon: Home,
    path: '/',
    exact: true,
  },
  {
    id: 'kpsea',
    label: 'KPSEA Papers',
    icon: BookOpen,
    path: '/papers/KPSEA',
    accent: '#2563eb',
    children: null,
    badge: 'Grade 6',
    badgeColor: '#2563eb',
  },
  {
    id: 'kjsea',
    label: 'KJSEA Papers',
    icon: GraduationCap,
    path: '/papers/KJSEA',
    accent: '#7c3aed',
    badge: 'Grade 9',
    badgeColor: '#7c3aed',
  },
  { type: 'divider' },
  {
    id: 'notes',
    label: 'Notes',
    icon: NotebookPen,
    accent: '#059669',
    comingSoon: true,
    children: [
      { id: 'notes-g1', label: 'Grade 1', path: '/notes/1', comingSoon: true },
      { id: 'notes-g2', label: 'Grade 2', path: '/notes/2', comingSoon: true },
      { id: 'notes-g3', label: 'Grade 3', path: '/notes/3', comingSoon: true },
      { id: 'notes-g4', label: 'Grade 4', path: '/notes/4', comingSoon: true },
      { id: 'notes-g5', label: 'Grade 5', path: '/notes/5', comingSoon: true },
      { id: 'notes-g6', label: 'Grade 6', path: '/notes/6', comingSoon: true },
      { id: 'notes-g7', label: 'Grade 7', path: '/notes/7', comingSoon: true },
      { id: 'notes-g8', label: 'Grade 8', path: '/notes/8', comingSoon: true },
      { id: 'notes-g9', label: 'Grade 9', path: '/notes/9', comingSoon: true },
    ],
  },
  {
    id: 'topical',
    label: 'Topical Revision',
    icon: Brain,
    accent: '#d97706',
    comingSoon: true,
    children: [
      { id: 'top-g1', label: 'Grade 1', path: '/topical/1', comingSoon: true },
      { id: 'top-g2', label: 'Grade 2', path: '/topical/2', comingSoon: true },
      { id: 'top-g3', label: 'Grade 3', path: '/topical/3', comingSoon: true },
      { id: 'top-g4', label: 'Grade 4', path: '/topical/4', comingSoon: true },
      { id: 'top-g5', label: 'Grade 5', path: '/topical/5', comingSoon: true },
      { id: 'top-g6', label: 'Grade 6', path: '/topical/6', comingSoon: true },
      { id: 'top-g7', label: 'Grade 7', path: '/topical/7', comingSoon: true },
      { id: 'top-g8', label: 'Grade 8', path: '/topical/8', comingSoon: true },
      { id: 'top-g9', label: 'Grade 9', path: '/topical/9', comingSoon: true },
    ],
  },
];

// ── NavItem component ──────────────────────────────────────────────────────────
const NavItem = ({ item, location, navigate, onClose }) => {
  const [open, setOpen] = useState(false);
  const isActive = item.path && (
    item.exact
      ? location.pathname === item.path || (location.pathname === '/' && item.path === '/')
      : location.pathname.startsWith(item.path)
  );

  if (item.children) {
    return (
      <div>
        <button
          onClick={() => !item.comingSoon && setOpen(v => !v)}
          style={{
            width: '100%',
            display: 'flex',
            alignItems: 'center',
            gap: '0.6rem',
            padding: '0.52rem 0.75rem',
            borderRadius: '0.6rem',
            border: 'none',
            background: 'none',
            cursor: item.comingSoon ? 'default' : 'pointer',
            color: item.comingSoon ? '#94a3b8' : '#334155',
            fontSize: '0.83rem',
            fontWeight: '600',
            transition: 'background 0.15s',
          }}
          onMouseEnter={e => { if (!item.comingSoon) e.currentTarget.style.background = '#f1f5f9'; }}
          onMouseLeave={e => { e.currentTarget.style.background = 'none'; }}
        >
          <span style={{
            width: '28px', height: '28px', borderRadius: '0.5rem',
            background: item.comingSoon ? '#f1f5f9' : `${item.accent}15`,
            display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0,
          }}>
            <item.icon size={14} color={item.comingSoon ? '#94a3b8' : item.accent} />
          </span>
          <span style={{ flex: 1, textAlign: 'left' }}>{item.label}</span>
          {item.comingSoon && (
            <span style={{
              fontSize: '0.6rem', fontWeight: '700', background: '#fef3c7',
              color: '#92400e', padding: '0.1rem 0.4rem', borderRadius: '4px',
              border: '1px solid #fde68a', whiteSpace: 'nowrap',
            }}>SOON</span>
          )}
          {!item.comingSoon && (open ? <ChevronUp size={13} /> : <ChevronDown size={13} />)}
        </button>

        {open && !item.comingSoon && (
          <div style={{ marginLeft: '2.1rem', marginTop: '0.15rem', display: 'flex', flexDirection: 'column', gap: '0.1rem' }}>
            {item.children.map(child => (
              <button
                key={child.id}
                onClick={() => { if (!child.comingSoon) { navigate(child.path); onClose(); } }}
                style={{
                  display: 'flex', alignItems: 'center', justifyContent: 'space-between',
                  padding: '0.38rem 0.65rem', borderRadius: '0.5rem',
                  border: 'none', background: 'none', cursor: child.comingSoon ? 'default' : 'pointer',
                  fontSize: '0.8rem', fontWeight: '500',
                  color: child.comingSoon ? '#94a3b8' : '#475569',
                  transition: 'background 0.15s',
                }}
                onMouseEnter={e => { if (!child.comingSoon) e.currentTarget.style.background = '#f1f5f9'; }}
                onMouseLeave={e => { e.currentTarget.style.background = 'none'; }}
              >
                <span>{child.label}</span>
                {child.comingSoon && <span style={{ fontSize: '0.58rem', color: '#94a3b8' }}>Soon</span>}
              </button>
            ))}
          </div>
        )}
      </div>
    );
  }

  return (
    <button
      onClick={() => { if (!item.comingSoon && item.path) { navigate(item.path); onClose(); } }}
      style={{
        width: '100%',
        display: 'flex',
        alignItems: 'center',
        gap: '0.6rem',
        padding: '0.52rem 0.75rem',
        borderRadius: '0.6rem',
        border: 'none',
        background: isActive ? `${item.accent || '#2563eb'}12` : 'none',
        cursor: item.comingSoon ? 'default' : 'pointer',
        color: isActive ? (item.accent || '#2563eb') : '#334155',
        fontSize: '0.83rem',
        fontWeight: isActive ? '700' : '600',
        transition: 'all 0.15s',
        borderLeft: isActive ? `3px solid ${item.accent || '#2563eb'}` : '3px solid transparent',
      }}
      onMouseEnter={e => { if (!isActive && !item.comingSoon) e.currentTarget.style.background = '#f1f5f9'; }}
      onMouseLeave={e => { if (!isActive) e.currentTarget.style.background = 'none'; }}
    >
      <span style={{
        width: '28px', height: '28px', borderRadius: '0.5rem',
        background: isActive ? `${item.accent || '#2563eb'}18` : '#f1f5f9',
        display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0,
      }}>
        <item.icon size={14} color={isActive ? (item.accent || '#2563eb') : '#64748b'} />
      </span>
      <span style={{ flex: 1, textAlign: 'left' }}>{item.label}</span>
      {item.badge && (
        <span style={{
          fontSize: '0.6rem', fontWeight: '800',
          background: `${item.badgeColor}15`, color: item.badgeColor,
          padding: '0.12rem 0.45rem', borderRadius: '9999px',
          border: `1px solid ${item.badgeColor}25`, whiteSpace: 'nowrap',
        }}>{item.badge}</span>
      )}
      {isActive && <ChevronRight size={13} style={{ opacity: 0.7 }} />}
    </button>
  );
};

// ── Sidebar content ────────────────────────────────────────────────────────────
const SidebarContent = ({ location, navigate, onClose }) => (
  <div style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
    {/* Logo */}
    <div style={{
      padding: '1rem 1rem 0.75rem',
      borderBottom: '1px solid #f1f5f9',
      display: 'flex', alignItems: 'center', gap: '0.6rem',
    }}>
      <div style={{
        width: '34px', height: '34px', borderRadius: '0.65rem',
        background: 'linear-gradient(135deg, #2563eb, #7c3aed)',
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        boxShadow: '0 4px 12px rgba(37,99,235,0.3)', flexShrink: 0,
      }}>
        <BookOpen size={16} color="#fff" strokeWidth={2.5} />
      </div>
      <div>
        <div style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '800', fontSize: '1rem', color: '#0f172a', lineHeight: 1.1 }}>
          CBC Portal
        </div>
        <div style={{ fontSize: '0.65rem', color: '#64748b', fontWeight: '500' }}>
          Offline Assessment Suite
        </div>
      </div>
    </div>

    {/* Nav items */}
    <nav style={{ flex: 1, padding: '0.6rem 0.5rem', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '0.15rem' }}>
      {NAV_ITEMS.map((item, i) => {
        if (item.type === 'divider') {
          return (
            <div key={`divider-${i}`} style={{ margin: '0.5rem 0.25rem', borderTop: '1px solid #f1f5f9' }}>
              <span style={{ fontSize: '0.6rem', fontWeight: '800', color: '#94a3b8', letterSpacing: '0.1em', textTransform: 'uppercase', padding: '0.4rem 0.5rem 0.2rem', display: 'block' }}>
                Learning Resources
              </span>
            </div>
          );
        }
        return <NavItem key={item.id} item={item} location={location} navigate={navigate} onClose={onClose} />;
      })}
    </nav>

    {/* Footer */}
    <div style={{
      padding: '0.75rem 1rem',
      borderTop: '1px solid #f1f5f9',
    }}>
      <div style={{
        display: 'flex', alignItems: 'center', gap: '0.4rem',
        background: '#f0fdf4', border: '1px solid #bbf7d0',
        borderRadius: '0.5rem', padding: '0.4rem 0.65rem',
        fontSize: '0.7rem', color: '#166534', fontWeight: '600',
      }}>
        <span style={{ width: '6px', height: '6px', borderRadius: '50%', background: '#22c55e', flexShrink: 0 }} />
        Offline Ready
        <Sparkles size={11} style={{ marginLeft: 'auto', opacity: 0.6 }} />
      </div>
    </div>
  </div>
);

// ── AppShell ────────────────────────────────────────────────────────────────────
export const AppShell = ({ children }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const [mobileOpen, setMobileOpen] = useState(false);

  // Close mobile sidebar on route change
  useEffect(() => {
    setMobileOpen(false);
  }, [location.pathname]);

  // Close on escape
  useEffect(() => {
    const handler = (e) => { if (e.key === 'Escape') setMobileOpen(false); };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, []);

  // Lock body scroll when mobile sidebar is open
  useEffect(() => {
    if (mobileOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => { document.body.style.overflow = ''; };
  }, [mobileOpen]);

  const closeSidebar = useCallback(() => setMobileOpen(false), []);

  return (
    <div className="app-shell">
      {/* ── Desktop Sidebar ── */}
      <aside className="sidebar-desktop">
        <SidebarContent location={location} navigate={navigate} onClose={closeSidebar} />
      </aside>

      {/* ── Mobile Backdrop ── */}
      {mobileOpen && (
        <div
          className="sidebar-backdrop"
          onClick={() => setMobileOpen(false)}
        />
      )}

      {/* ── Mobile Sidebar Drawer ── */}
      <aside className={`sidebar-mobile ${mobileOpen ? 'sidebar-mobile-open' : ''}`}>
        <div style={{ display: 'flex', justifyContent: 'flex-end', padding: '0.6rem 0.75rem 0' }}>
          <button
            onClick={() => setMobileOpen(false)}
            style={{
              background: '#f1f5f9', border: 'none', borderRadius: '0.5rem',
              width: '32px', height: '32px', display: 'flex', alignItems: 'center',
              justifyContent: 'center', cursor: 'pointer', color: '#64748b',
            }}
          >
            <X size={16} />
          </button>
        </div>
        <SidebarContent location={location} navigate={navigate} onClose={closeSidebar} />
      </aside>

      {/* ── Main Column ── */}
      <div className="main-column">
        {/* Mobile top bar */}
        <header className="mobile-topbar">
          <button
            onClick={() => setMobileOpen(true)}
            style={{
              background: 'none', border: 'none', cursor: 'pointer',
              padding: '0.4rem', borderRadius: '0.4rem',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              color: '#334155',
            }}
          >
            <Menu size={22} />
          </button>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <div style={{
              width: '28px', height: '28px', borderRadius: '0.5rem',
              background: 'linear-gradient(135deg, #2563eb, #7c3aed)',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
            }}>
              <BookOpen size={14} color="#fff" strokeWidth={2.5} />
            </div>
            <span style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '800', fontSize: '0.95rem', color: '#0f172a' }}>
              CBC Portal
            </span>
          </div>
          <div style={{ width: '34px' }} />
        </header>

        {/* Page content */}
        <main className="shell-content">
          {children}
        </main>
      </div>
    </div>
  );
};
