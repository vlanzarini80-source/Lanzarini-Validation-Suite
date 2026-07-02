import json
import time
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
JSON_DIR = ROOT / "results" / "json"
REPORT_DIR = ROOT / "results" / "reports"

JSON_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

OUT_JSON = JSON_DIR / "v1f_validation_report_summary.json"
OUT_MD = REPORT_DIR / "validation_suite_v1_report.md"
OUT_HTML = REPORT_DIR / "validation_suite_v1_report.html"

INPUTS = {
    "V1A": (JSON_DIR / "v1a_environment_report.json", "pass_v1a"),
    "V1B": (JSON_DIR / "v1b_adapter_contract_report.json", "pass_v1b"),
    "V1C": (JSON_DIR / "v1c_micro_correctness_report.json", "pass_v1c"),
    "V1D": (JSON_DIR / "v1d_runtime_smoke_report.json", "pass_v1d"),
    "V1E": (JSON_DIR / "v1e_artifact_manifest_report.json", "pass_v1e"),
}


def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def yesno(value: bool) -> str:
    return "PASS" if value is True else "FAIL"


def main() -> None:
    missing_inputs = []
    stage_status = {}
    reports = {}

    for stage, (path, key) in INPUTS.items():
        if not path.exists():
            missing_inputs.append(str(path))
            stage_status[stage] = False
            reports[stage] = None
            continue

        data = load_json(path)
        reports[stage] = data
        stage_status[stage] = data.get(key) is True

    all_pass = len(missing_inputs) == 0 and all(stage_status.values())

    summary = {
        "stage": "V1F_VALIDATION_REPORT_GENERATOR",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "root": str(ROOT),
        "missing_inputs": missing_inputs,
        "all_pass_v1a_to_v1e": all_pass,
        "report_markdown": str(OUT_MD),
        "report_html": str(OUT_HTML),
        "stage_status": stage_status,
        "strict_note": (
            "V1F generates a report from public validation artifacts only. "
            "It does not import, read, hash, or expose private kernel source code."
        ),
    }

    md_lines = []
    md_lines.append("# Lanzarini Validation Suite v1.0 Report")
    md_lines.append("")
    md_lines.append(f"Generated at: `{summary['timestamp']}`")
    md_lines.append("")
    md_lines.append("## Stage Status")
    md_lines.append("")
    md_lines.append("| Stage | Status |")
    md_lines.append("|---|---|")

    for stage in INPUTS:
        md_lines.append(f"| {stage} | {yesno(stage_status.get(stage, False))} |")

    md_lines.append("")
    md_lines.append("## Summary")
    md_lines.append("")
    md_lines.append(f"- All V1A to V1E passed: `{all_pass}`")
    md_lines.append(f"- Missing inputs: `{len(missing_inputs)}`")
    md_lines.append("")
    md_lines.append("## Strict Interpretation")
    md_lines.append("")
    md_lines.append(summary["strict_note"])
    md_lines.append("")

    for stage, data in reports.items():
        md_lines.append(f"## {stage}")
        md_lines.append("")
        if data is None:
            md_lines.append("Missing input report.")
            md_lines.append("")
            continue

        md_lines.append("```json")
        md_lines.append(json.dumps(data, indent=2))
        md_lines.append("```")
        md_lines.append("")

    OUT_MD.write_text("\n".join(md_lines), encoding="utf-8")

    html_body = "<h1>Lanzarini Validation Suite v1.0 Report</h1>\n"
    html_body += f"<p>Generated at: <code>{escape(summary['timestamp'])}</code></p>\n"
    html_body += "<h2>Stage Status</h2>\n"
    html_body += "<table border='1' cellpadding='6' cellspacing='0'>"
    html_body += "<tr><th>Stage</th><th>Status</th></tr>"

    for stage in INPUTS:
        html_body += (
            "<tr>"
            f"<td>{escape(stage)}</td>"
            f"<td>{escape(yesno(stage_status.get(stage, False)))}</td>"
            "</tr>"
        )

    html_body += "</table>\n"
    html_body += "<h2>Summary</h2>\n"
    html_body += f"<p>All V1A to V1E passed: <code>{escape(str(all_pass))}</code></p>\n"
    html_body += f"<p>Missing inputs: <code>{escape(str(len(missing_inputs)))}</code></p>\n"
    html_body += "<h2>Strict Interpretation</h2>\n"
    html_body += f"<p>{escape(summary['strict_note'])}</p>\n"

    for stage, data in reports.items():
        html_body += f"<h2>{escape(stage)}</h2>\n"
        if data is None:
            html_body += "<p>Missing input report.</p>\n"
        else:
            html_body += "<pre>"
            html_body += escape(json.dumps(data, indent=2))
            html_body += "</pre>\n"

    OUT_HTML.write_text(
        "<html><head><meta charset='utf-8'>"
        "<title>Lanzarini Validation Suite v1.0 Report</title>"
        "</head><body>"
        + html_body
        + "</body></html>",
        encoding="utf-8",
    )

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print("=" * 80)
    print("LANZARINI VALIDATION SUITE v1.0 - V1F REPORT GENERATOR")
    print("=" * 80)
    print(json.dumps(summary, indent=2))
    print("=" * 80)
    print("MARKDOWN:", OUT_MD)
    print("HTML:", OUT_HTML)
    print("JSON:", OUT_JSON)
    print("PASS_V1F:", all_pass)
    print("=" * 80)

    if not all_pass:
        raise SystemExit("V1F FAILED: one or more V1A-V1E inputs missing or not passing")

    print("V1F PASSED")


if __name__ == "__main__":
    main()
